from django.shortcuts import render, redirect, get_object_or_404
from Employee.models import User
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import AbstractUser
from django.db import models
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
from django.core.mail import EmailMessage
import random
import string
from .forms import AssetForm
from .models import Assets
from .models import Assign
from .forms import AssignForm
from django.urls import reverse


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
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=firstname, last_name=lastname)
            user.role = role
            user.save()
            login(request, user)
            return render(request, 'Employee/Frontpage/sigin.html')
    return render(request, 'Employee/Frontpage/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return (render, 'signup')
    
    return render(request, 'Employee/Frontpage/sigin.html')


def home(request):
    employees = Employee.objects.all()
    assets = Assets.objects.all()
    # employee = get_object_or_404(Employee)
    # assetsAssigned = employee.assignment.set.all()
    # if employee_id:
    #     employee = get_object_or_404(Employee, employee_id=employee_id)
        
    # else:
    #     employee = None     
    context = {
        'employees': employees,
        'assets': assets,
        # 'employee': employee,
        # 'assetsAssigned': assetsAssigned,
            }    
    return render(request, 'Employee/Frontpage/home.html',context)


def generate_random_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation
    temporary_password = ''.join(random.choice(characters)
                                 for _ in range(length))
    return temporary_password


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  
            temporary_password = generate_random_password()
            # send_email_password(employee.email, temporary_password)
            return redirect('home')
        else:
            messages.error(request, 'The form is Invalid')
            return redirect('add_employee')
        form = EmployeeForm()
    return render(request, 'Employee/partials/add_employee.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'Employee/partials/employee_list.html', {'employees': employees})


def update_employee(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    context = {
        'form': form,
        'employee_id': employee_id,
        'employee': employee,
    }
    return render(request, 'Employee/partials/update_employee.html', context)


def remove_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    else:
        pass


def send_email_password(employee_email, temporary_password):
    from_email = 'celinediego19@gmail.com'
    subject = 'TEMPORARY PASSWORD'
    message = f'Greetings, your temporary password is: {temporary_password}. Please login using this password and change it immediately.'
    to_email = [employee_email]

    email = EmailMessage(subject, from_email, message, to_email)
    email.send()


def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
      form = AssetForm()
    context = {
        'form': form
    }

    return render(request, 'Employee/partials/add_asset.html',context)


def assign_asset(request):
    if request.method == 'POST':
        form  = AssignForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee']
            asset_id = form.cleaned_data['asset']
            assigned_date = form.cleaned_data['assigned_date']
            
            assignement = Assign(employee = employee_id, asset = asset_id, assigned_date = assigned_date )
            assignement.save()
            return redirect('home')
    else:
        form = AssignForm()
        
    return render(request, 'Employee/partials/assign_asset.html', {'form': form} )


