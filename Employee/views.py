from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Employee.decorators import allowed_users, unauthenticated_user
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
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import check_password



User = get_user_model()
User.add_to_class('is_employer', models.BooleanField(default=False))
User.add_to_class('is_employee', models.BooleanField(default=False))

# Create your views here.

# @unauthenticated_user
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
            group = Group.objects.get(name='Employers')
            user.groups.add(group)
            user.save()
            login(request, user)
            return render(request, 'Employee/Frontpage/sigin.html')
    return render(request, 'Employee/Frontpage/signup.html')


from django.contrib.auth import login, authenticate 
from django.shortcuts import redirect

# @unauthenticated_user
def signin(request):

  if request.method == 'POST':

    username = request.POST['username']
    password = request.POST['password']
        
    user = authenticate(request, username=username, password=password)

    if user is not None:
        
      login(request, user)
      return redirect('home')
  return render(request, 'Employee/Frontpage/sigin.html')
            

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import Employee

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import Employee

def employee_signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        temporary_password = request.POST['temporary_password']
        
        try:
            employee = Employee.objects.get(username=username)
        except Employee.DoesNotExist:
            employee = None
            
        if employee is not None:
            user = authenticate(request, username=username, password=temporary_password)
            if user is not None:
                login(request, user)
                print("User authenticated")
                return redirect('home')
            else:
                print("Authentication failed")
        else:
            print("Password mismatch or employee not found")
            
    return render(request, 'Employee/Frontpage/employee_signin.html')

@allowed_users(allowed_roles=['Employers','Employees'])
def home(request):
    
    employees = Employee.objects.all()
    assets = Assets.objects.all()
    for employeees in Employee.objects.all():
        assigned_asset = employeees.assignments.all()
        for asset in assigned_asset:
            print("Asset Name:", asset.asset_name.asset_name," Assigned to", employeees.username )
            
    if request.user.is_authenticated:
        username = request.user.username
        
    
       
    
    context = {
        'employees': employees,
        'assets': assets,
        'assigned_asset' : assigned_asset,
        'username' : username,
        # 'employee': employee,
        
            }    
    return render(request, 'Employee/Frontpage/home.html',context)
@allowed_users(allowed_roles=['Employers','Employees'])
def employee_assets(request, employee_id):
    # This function will display the list of all assets that are assigned
    individual_employee = Employee.objects.get(employee_id = employee_id)
    assetes  = individual_employee.assignments.all()
    
    context = {
        'assigned' : assetes,
        'employ' : individual_employee
    }
    
    return render(request,'Employee/partials/employee_assets.html',context)


def generate_random_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation
    temporary_password = ''.join(random.choice(characters)
                                 for _ in range(length))
    print('temporary_password')
    return temporary_password

@allowed_users(allowed_roles=['Employers'])
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            temporary_password = form.cleaned_data['temporary_password']
            user = User.objects.create_user(username=username, password=temporary_password)
            group = Group.objects.get(name='Employees')
            user.groups.add(group)
            user.save()
            form.save()
            return redirect('home')
        else:
            return HttpResponse('The form is Invalid')
            return redirect('add_employee')
    
        #   return redirect('home') 
            # temporary_password = generate_random_password()
            # print('random_password',temporary_password)
            # send_email_password(employee.email, temporary_password)
        
    return render(request, 'Employee/partials/add_employee.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'Employee/partials/employee_list.html', {'employees': employees})

@allowed_users(allowed_roles=['Employers','Employees'])
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

@allowed_users(allowed_roles=['Employers'])
def remove_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
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

@allowed_users(allowed_roles=['Employers'])
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
@allowed_users(allowed_roles=['Employers'])
def remove_asset(request, asset_id):
    
    asset = get_object_or_404(Assets,asset_id=asset_id)
    if request.method == 'POST':
        asset.delete()
        return redirect('home')
    else:
        pass

@allowed_users(allowed_roles=['Employers']) 
def assign_asset(request):
    if request.method == 'POST':
        form  = AssignForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee']
            asset_name = form.cleaned_data['asset_name']
            assigned_date = form.cleaned_data['assigned_date']
            
            assignement = Assign(employee = employee_id, asset_name = asset_name, assigned_date = assigned_date )
            assignement.save()
        return redirect('home')
    else:
        form = AssignForm()
        
    return render(request, 'Employee/partials/assign_asset.html', {'form': form} )

def employee_dashboard(request):
    
    if request.user.is_authenticated and request.user.is_employees:
        
     return render(request, 'Employee/Frontpage/employee_home.html')






