from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


""" def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form}) """

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            # Passwords don't match, handle the error appropriately
            return render(request, 'registration/register.html', {'error_message': 'Passwords do not match'})

        # Create a new User object and save it to the database
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Redirect to the login page after successful registration
        return redirect('login')

    # If the request method is GET, render the registration form
    return render(request, 'registration/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('resume')  # Redirect to the profile page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

""" @login_required
def profile(request):
    # Logic to display user profile information
    return render(request, 'registration/profile.html')
 """

def homepage(request):
    # Logic for your homepage view goes here
    # For now, let's just render the homepage template
    return render(request, 'index.html')

def resume(request):
    return render(request, 'resume.html')

#Create a custom error handler function 
def csrf_failure(request, reason=""):
    return render(request, 'csrf_failure.html', {'reason': reason})