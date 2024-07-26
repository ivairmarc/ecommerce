from django.shortcuts import render
from django.urls import reverse_lazy
from website.models import Employees
from website.forms import EmployModelForm
from django.views.generic import ListView, CreateView


class EmployeesList(ListView):
    model = Employees
    template_name = 'website/_layouts/employees.html'
    context_object_name = 'employees'


class EmployCreate(CreateView):
    model = Employees
    form_class = EmployModelForm
    template_name = 'website/_layouts/new_employ.html'
    success_url = '/employees/'
    
