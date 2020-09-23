from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from testapp.models import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from testapp.forms import *
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

from django.forms.models import inlineformset_factory
EmployeeEduFormset = inlineformset_factory(
    Employee, EmployeeEducationDetail, fields=('degree','college','college_start_year','college_start_month','college_end_year','college_end_month','currently_pursuing',)
)

EmployeeWorkFormset = inlineformset_factory(
    Employee, EmployeeWorkDetail, fields=('company_name','comp_start_year','comp_start_month','comp_end_year','comp_end_month','currently_working',)
)

class EmployeeCreateView(CreateView):
    template_name = 'employee_create.html'
    model = Employee
    fields = ["first_name",'last_name','dob','other','resume']

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["empducationdetail"] = EmployeeEduFormset(self.request.POST)
            data["empworkdetail"] = EmployeeWorkFormset(self.request.POST)
        else:
            data["empducationdetail"] = EmployeeEduFormset()
            data["empworkdetail"] = EmployeeWorkFormset()
        return data
    def form_valid(self, form):
        context = self.get_context_data()
        empducationdetail = context["empducationdetail"]
        empworkdetail = context["empworkdetail"]
        self.object = form.save()
        if empducationdetail.is_valid():
            empducationdetail.instance = self.object
            empducationdetail.save()
        if empworkdetail.is_valid():
            empworkdetail.instance = self.object
            current_start_year = int(empworkdetail.comp_start_year)
            current_start_month = int(empworkdetail.comp_start_month)
             
            if EmployeeWorkDetail.objects.filter(employee= self.object,comp_end_year = current_start_year).filter(comp_end_month__gt = current_start_month).exists():
                empworkdetail.save()
            elif EmployeeWorkDetail.objects.filter(employee= self.object,comp_end_year__lt = current_start_year).exists():
                empworkdetail.save()
            
            
        return super().form_valid(form)
    def get_success_url(self):
        return HttpResponseRedirect('')


class EmployeeListView(ListView):
    template_name = 'employee_list.html'
    model =Employee


class EmployeeDeleteView(DeleteView):
    template_name = 'employee_confirm_delete.html'
    model = Employee
class EmployeeWorkDeleteView(DeleteView):
    template_name = 'employeework_confirm_delete.html'
    model = EmployeeWorkDetail


class EmployeeEducationDeleteView(DeleteView):
    template_name = 'employeeeducation_confirm_delete.html'
    model = EmployeeEducationDetail

class EmployeeUpdateView(UpdateView):
    template_name = 'employee_form.html'
    model=Employee
    fields=["first_name",'last_name','dob','other','resume']

class EmployeeEducationUpdateView(UpdateView):
    template_name = 'employeeeducation_form.html'
    model=EmployeeEducationDetail
    fields=['degree','college','college_start_year','college_start_month','college_end_year','college_end_month','currently_pursuing']

class EmployeeWorkUpdateView(UpdateView):
    template_name = 'employeework_form.html'
    model= EmployeeWorkDetail
    fields=['company_name','comp_start_year','comp_start_month','comp_end_year','comp_end_month','currently_working']


