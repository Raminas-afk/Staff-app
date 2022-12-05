from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Employee, Event
from .forms import NewEmployeeForm, NewEventForm

from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer

from django.http import JsonResponse

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

class AddNewEventView(LoginRequiredMixin, CreateView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    model = Event
    form_class = NewEventForm
    template_name = "employees/new_event.html"
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
def department_list(request, department):
    if request.method == "GET":
        department_employees = Employee.objects.filter(department__name=department)
        return render(request, "employees/department_list.html", {
        "employees": department_employees,
        "department": department
        })

@login_required(login_url="/user/login_user")
def event_list(request):
    if request.method == "GET":
        events = Event.objects.all()
        return render(request, "employees/event_list.html", {
            "events": events
        })
        #1 management 2 hr 3 accounting 5 logistics 6 warehouse

class AddNewEventView(LoginRequiredMixin, CreateView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    model = Event
    form_class = NewEventForm
    template_name = "employees/new_event.html"
    success_url = "/events"

class EditEventView(LoginRequiredMixin, UpdateView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    model = Event
    fields = "__all__"
    template_name = "employees/edit_event.html"
    success_url = "/events"

class DeleteEventView(LoginRequiredMixin, DeleteView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    model=Event
    success_url = "/events"

class SpecificEventView(LoginRequiredMixin, DetailView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    template_name = "employees/specific_event.html"
    model = Event
    context_object_name= "event"
    


# Serializer ViewSets

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = [permissions.IsAuthenticated]

@api_view(['GET','POST'])    
def employee_list_api(request):
    if request.method == "GET":
        employees = Employee.objects.all()
    
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def specific_employee_api(request, id):
    try:
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

