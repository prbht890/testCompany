from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from testapp.models import *




# class EmployeeEducationForm(ModelForm):
#     class Meta:
#         model = EmployeeEducationDetail
#         fields = "__all__"

# class EmployeeWorkDetailForm(ModelForm):
#     class Meta:
#         model = EmployeeEducationDetail
#         fields = ['company_name','comp_start_year','comp_start_month','comp_end_year','comp_end_month',' currently_working',]

# class EmployeeForm(ModelForm):
#     employeeducation = EmployeeEducationForm(many= True)
#     employeeworkdetail = EmployeeEducationForm(many= True)
#     class Meta:
#         model = Employee
#         fields = '__all__'