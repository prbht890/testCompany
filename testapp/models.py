from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=255,null = True)
    last_name = models.CharField(max_length=255,null = True)
    dob = models.DateField(null = True)
    other = models.CharField(max_length=255,null = True)
    resume = models.ImageField(upload_to='documents/',null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="employees"

class EmployeeEducationDetail(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    degree = models.CharField(max_length=6655,null = True)
    college = models.CharField(max_length=6655,null = True)
    college_start_year = models.IntegerField(null = True)
    college_start_month = models.IntegerField(null = True)
    college_end_year = models.IntegerField(null = True)
    college_end_month = models.IntegerField(null = True)
    currently_pursuing = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class EmployeeWorkDetail(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=6000,null = True)
    comp_start_year = models.CharField(max_length=255,null = True)
    comp_start_month = models.CharField(max_length=255,null = True)
    comp_end_year = models.CharField(max_length=255,null = True)
    comp_end_month = models.CharField(max_length=255,null = True)
    currently_working = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    