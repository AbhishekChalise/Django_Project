from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import Http404
# Create your views here.

def register(request):
    print("Request Method:", request.method)  # Debugging
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log the user in after successful registration
            print("User registered and logged in successfully")
            return redirect('showTeacher')  # Redirect to another page (URL name should match your `urls.py`)
        else:
            print("Form is not valid:", form.errors)  # Debugging invalid form
            messages.error(request,'Values given are not correct!!!')
            return redirect('register')

    else:
        form = SignUpForm()
    
    return render(request, 'registration.html', {'form': form})
        
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib import messages

def Login(request):
    print('Hello')  # Debugging log
    print("Request Method:", request.method)  # Debugging log
    
    if request.method == "POST":
        print("Processing POST request in login")
        
        username = request.POST.get('username')  # Safely retrieve username
        password = request.POST.get('password')  # Safely retrieve password

        user = authenticate(request, username=username, password=password)  # Authenticate user
        
        if user:  # If user authentication succeeds
            login(request, user)  # Log the user in
            print(f"User {username} logged in successfully")
            return redirect('showTeacher')  # Redirect to the showTeacher page
        else:
            print("Authentication failed")  # Debugging log
            messages.error(request, "Invalid Username or Password.")  # Add error message
            raise Http404("User Does not Exists!!!")
        #   raise ValidationError("Error Invalid Username or Password")

    return render(request, 'Login.html')


        
@login_required (login_url = '/Login/')
def logout_view(request):
    logout(request)
    return redirect('login')

    
    


