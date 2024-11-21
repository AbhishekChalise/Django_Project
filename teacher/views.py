from django.shortcuts import render
from teacher.forms import Teacher_forms
from django.shortcuts import redirect
from teacher.models import Teacher
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

# Note Very important thing you cannot put the Class name and the Form name same.

def home_view(request):
    return render(request,'home.html')

@login_required (login_url = '/Login/')
def Teachers(request):
    if request.method == 'GET':
        form = Teacher_forms()
        return render(request,'Teacher_index.html',{'form':form})
    elif request.method == 'POST':
        form = Teacher_forms(request.POST)
        print('We have Successfully applied the get and post method')
        if form.is_valid():
            print('Here we are at 2')
            try:
                print('Hi inside the try block')
                teacher_instance = form.save()
                request.session['teacher']  ={ # Here We have created a Sessions. Which will hold the Session data.
                    'tid' : str(teacher_instance.Tid),
                    'tname' : str(teacher_instance.Tname),
                    'temail' : str(teacher_instance.Temail),
                    'tcontact': str(teacher_instance.Tcontact),
                }
                return redirect('showTeacher') # Aba eta teacher ko data haru show garna lai rakhna parxa.
            except Exception as e:
                 print(f"Error while saving form: {e}") 
                 return render(request , 'Teacher_index.html',{'form':form})
        else:
            print('Invalid form Submission')
            return render(request , 'Teacher_index.html',{'form':form}) # This renders another html page when there is invalid form submission
        
# This is the method for the rendering the post request.

@login_required (login_url = '/Login/')
def Show_teacher(request):
    print(f"Is User Logged In: {request.user.is_authenticated}")
    teacher_obj = Teacher.objects.filter( Tdeleted = False)
    print(teacher_obj)
    teacher_session = request.session.get(Teachers)
    context = {
        'teacher_obj': teacher_obj,
        'teacher_session': teacher_session 
    }
    return render(request , 'Teacher_Show.html', context)

def edit_teacher(request, id):
    # Get the teacher instance by ID
    print(f"Editing teacher with ID: {id}")
    teacher = Teacher.objects.filter(id=id).last()
    print(teacher.id, "Teacher")

    # Use get_object_or_404 to get the teacher by id (instead of Tid)
    get_instance = get_object_or_404(Teacher, id=id)

    if request.method == 'GET':
        # Render the edit form with the existing instance
        form = Teacher_forms(instance=get_instance)
        context = {
            'form': form,
            'teacher': get_instance
        }
        return render(request, 'Teacher_edit.html', context)

    elif request.method == 'POST':
        # Update the teacher instance with the submitted data
        form = Teacher_forms(request.POST, instance=get_instance)
        if form.is_valid():
            form.save()
            # Redirect to the show page after successful edit
            return redirect('showTeacher')
        else:
            # Re-render the edit form with errors
            context = {
                'form': form,
                'teacher': get_instance,
                'error': 'Please correct the errors below.'
            }
            return render(request, 'Teacher_edit.html', context)

def delete_teacher(request,id):
    teacher_instance = Teacher.objects.filter(id=id).last()
    teacher_instance.Tdeleted = True
    teacher_instance.save()
    # teacher_instance.delete()
    return redirect('showTeacher')


# return of .get
# .filter
# return of .all
