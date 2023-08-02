




from django.db import models
# from .models import Employee, Assets

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True, default='')
    role = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=100)
    
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email  = models.EmailField(max_length=100, default='')
    username = models.CharField(max_length=255, unique=True, default='employee')
    phonenumber = models.IntegerField()
    role = models.CharField(max_length=100)
    temporary_password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Assets(models.Model):
    asset_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100,unique=True)

class Assign(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="assignments" )
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE, related_name="assets" )
    assigned_date = models.DateField()
    
    def __str__(self):
        return f"{self.employee_id} - {self.asset_id}" 
    
    
    
    
    
    
    
    
         
    

    