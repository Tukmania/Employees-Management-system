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
        fields = ['asset_id','asset_name','serial_number']
        
class AssignForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(),empty_label=None, to_field_name='employee_id')
    asset_name = forms.ModelChoiceField(queryset=Assets.objects.values_list('asset_name' ,flat=True),empty_label=None, to_field_name='asset_name')
    assigned_date = forms.DateField()
    