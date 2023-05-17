from django.shortcuts import render
from Employee.models import User

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        role = request.POST['role']
        companyname = request.POST['companyname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
                
        user = User(firstname = firstname, lastname = lastname, role =  role, companyname = companyname,
                    email = email, phone = phone)
        user.save()
        
        return render(request, 'Frontpage/signup_success.html')
    else:
        
        return render(request, 'Frontpage/signup.html')
