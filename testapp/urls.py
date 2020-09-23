from django.urls import path

from .import views

urlpatterns = [
     path('employee_create',views.EmployeeCreateView.as_view()),
     path('employee_list',views.EmployeeListView.as_view()),
     path('employee/edit/<int:pk>',views.EmployeeUpdateView.as_view()),
     path('employeework/edit/<int:pk>',views.EmployeeWorkUpdateView.as_view()),
     path('employeeeducation/edit/<int:pk>',views.EmployeeEducationUpdateView.as_view()),
     path('employee/delete/<int:pk>',views.EmployeeDeleteView.as_view()),
     path('employeework/delete/<int:pk>',views.EmployeeWorkDeleteView.as_view()),
     path('employeeeducation/delete/<int:pk>',views.EmployeeEducationDeleteView.as_view())

     
]