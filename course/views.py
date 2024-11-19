from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from course.forms import course_forms
from course.models import Course
from django.http import HttpResponse

# Create your views here.

def Teachers(request):
    if request.method == 'GET':
        form = course_forms()
        return render(request,'Teacher_index.html',{'form':form})
    elif request.method == 'POST':
        form = course_forms(request.POST)
        print('We have Successfully applied the get and post method')
        if form.is_valid():
            print('Here we are at 2')
            try:
                print('Hi inside the try block')
                teacher_instance = form.save()
                request.session['course']  ={ # Here We have created a Sessions. Which will hold the Session data.
                    'tid' : str(teacher_instance.Tid),
                    'tname' : str(teacher_instance.Tname),
                    'temail' : str(teacher_instance.Temail),
                    'tcontact': str(teacher_instance.Tcontact),
                }
                return redirect('course') # Aba eta teacher ko data haru show garna lai rakhna parxa.
            except Exception as e:
                 print(f"Error while saving form: {e}") 
                 return render(request , 'Teacher_index.html',{'form':form})
        else:
            print('Invalid form Submission')
            return render(request , 'Teacher_index.html',{'form':form})