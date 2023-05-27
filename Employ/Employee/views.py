from django.shortcuts import render, redirect
from Employee.models import User
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import AbstractUser
from django.db import models



User = get_user_model()

# Create your views here.
def signup(request):
    
  if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        role = request.POST.get('role')
        if username and password and email and firstname and lastname and role:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
            user.role = role
            user.save()
            login(request, user)
            return render(request, 'Employee/Frontpage/sigin.html')
  return render(request, 'Employee/Frontpage/signup.html')


def signin(request):
  if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return(render, 'Employe')
  return render(request, 'Employee/Frontpage/sigin.html')

def home(request):
  return render(request, 'Employee/Frontpage/home.html')
        
        
          
