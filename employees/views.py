from django.shortcuts import render
from .forms import NewEmployeeForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EmployeeSerializer
# Create your views here.


class EmployeeListView(LoginRequiredMixin, ListView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    template_name = "employees/employee_list.html"
    model = Employee
    context_object_name = "employees_list"

class SpecificEmployeeView(LoginRequiredMixin, DetailView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    template_name = "employees/specific_employee.html"
    model = Employee
    context_object_name= "employee"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Employee info successfully changed"
        return context

class AddNewEmployeeView(LoginRequiredMixin, CreateView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    model = Employee
    form_class = NewEmployeeForm
    template_name = "employees/new_employee.html"
    success_url = "/"


 
class EditEmployeeView(LoginRequiredMixin, UpdateView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    model = Employee
    fields = "__all__"
    template_name = "employees/edit_employee.html"
    success_url = "/"


class DeleteEmployeeView(LoginRequiredMixin, DeleteView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    model=Employee
    success_url = "/"


@login_required(login_url="/user/login_user")
def DepartmentList(request, department):
    if request.method == "GET":
        department_employees = Employee.objects.filter(department=department)
        return render(request, "employees/department_list.html", {
        "employees": department_employees,
        "department": department
        })


        #1 management 2 hr 3 accounting 5 logistics 6 warehouse

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]