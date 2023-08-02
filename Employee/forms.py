from django import forms
from .models import Employee
from .models import Assets

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id','firstname','lastname','email','username','phonenumber','role','temporary_password']
        
class AssetForm(forms.ModelForm):
    class Meta:
        model = Assets
        fields = ['asset_id','name','serial_number']
        
class AssignForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(),empty_label=None, to_field_name='employee_id')
    asset = forms.ModelChoiceField(queryset=Assets.objects.all(),empty_label=None, to_field_name='asset_id')
    assigned_date = forms.DateField()
    