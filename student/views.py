from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from student.forms import student_forms
from student.models import Student
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# Create operation: 
# Here we have created a session and printed all the data in the page. 
@login_required(login_url = '/Login/')
def student(request):
    if request.method == 'POST':
        print('We are here 1')
        form = student_forms(request.POST)
        if form.is_valid():
            print('We are here 2')
            try:
                student_instance = form.save()
                # Create a Session in django.
                request.session['student'] = {
                    'sid':str(student_instance.sid),
                    'sname':str(student_instance.sname),
                    'semail':str(student_instance.semail),
                    'contact':str(student_instance.scontact),
                }
                return redirect('show') # Redirect to this page # return render(request , )
            except Exception as e:
                print('Not able to successfully connect')
            return render(request , '/error.html', {'error':'Could not save data!!!'})
        else:
            print('Invalid Form Submission:')
            return render(request , )
    else:
        form = student_forms()
        print('I am inside a get request')
        return render(request , 'index.html' ,{'form':form})
        # return(request , 'index.html') #This is the   # Finally return to the same login page. If there occurs any error.
 
 # This is Show.html file.
@login_required(login_url = '/Login/')
def show(request):
    # Here a session is defined.
    student_obj = Student.objects.filter(sdelete = False)
    student_session = request.session.get(student)
    context = {
        'student_obj':student_obj,
        'student_session':student_session
    }
    return render(request,'show.html',context)

from django.shortcuts import render, get_object_or_404, redirect
from student.forms import student_forms
from student.models import Student

def edit_students(request, id):
    # Get the student instance by ID
    get_instance = get_object_or_404(Student, id=id)

    if request.method == 'GET':
        # Render the edit form with the existing instance
        form = student_forms(instance=get_instance)
        context = {
            'form': form,
            'student': get_instance
        }
        return render(request, 'edit.html', context)

    elif request.method == 'POST':
        # Update the student instance with the submitted data
        form = student_forms(request.POST, instance=get_instance)
        if form.is_valid():
            form.save()
            # Redirect to the show page after successful edit
            return redirect('show')
        else:
            # Re-render the edit form with errors
            context = {
                'form': form,
                'student': get_instance,
                'error': 'Please correct the errors below.'
            }
            return render(request, 'edit.html', context)

def delete(request,id):
    student = Student.objects.get(id = id)
    student.sdelete = True
    # student.delete()
    student.save()
    return redirect('show')


        







