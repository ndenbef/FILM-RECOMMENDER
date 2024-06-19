
# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

from registration.models import User

from registration.forms import CustomUserCreationForm
from .models import *
from .forms import CustomUserCreationForm




# Create your views here.

def inscription(request): 
    
    form = CustomUserCreationForm()
    print("hello_1")
    
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST) 
        print("hello_2")
        print(request.POST)  # print the form data
        form.full_clean()  # validate the form manually
        print(form.errors)  # print any form errors
        
        if form.is_valid(): 
            print("hello_3")
            user = form.save(commit=False) 
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password']) 
            user.genre1 = ', '.join(form.cleaned_data.get('genre1')) 
            user.genre2 = ', '.join(form.cleaned_data.get('genre2'))
            print("hello_4")
            user.save() 
            
            print("hello_5")
            
            # new_user = User.objects.create(
            #     first_name=user.first_name,
            #     last_name=user.last_name,
            #     username=user.username,
            #     password=make_password(form.cleaned_data['password']),
            #     genre1=user.genre1,
            #     genre2=user.genre2
            # )
            
            login(request, user)
            
            return redirect('film:homepage') 
        
    return render(request, 'registration/register.html', {'form': form}) 

# # Define a view function for the home page
# def home(request):
#     return render(request, 'film/base.html')
 
# # Define a view function for the login page
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('film:homepage')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'registration/login.html')

@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('reg:login') # Redirect to your login view
    return render(request, 'registration/logout.html') # Render your logout template
 
# # Define a view function for the registration page
# def register_page(request):
    
#     numbers = list(range(10, 90))
    
#     # Check if the HTTP request method is POST (form submission)
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             nom = request.POST.get('first_name')
#             prenom = request.POST.get('last_name')
#             age = request.POST.get('ages')
#             genre = request.POST.getlist('genre')
#             genres = ', '.join(genre)
#             username = request.POST.get('username')
#             password = request.POST.get('password')
            
        
#             print(age)
#             print(genres)
        
         
#             # Check if a user with the provided username already exists
#             user = User.objects.filter(username=username)
            
#             if user.exists():
#                 # Display an information message if the username is taken
#                 messages.info(request, "Username already taken!")
#                 return redirect('/register/')
            
#             # User = get_user_model()
         
#             # Set the user's password and save the user object
#             user.set_password(password)
#             user.save()
         
#             # Display an information message indicating successful account creation
#             messages.info(request, "Account created Successfully!")
#             return redirect('/login/')
#     else :
#         form = CustomUserCreationForm()
            
     
#     # Render the registration page template (GET request)
#     return render(request, 'registration/register.html', {'agess': numbers, 'form': form})