from django.shortcuts import render
from .forms import NewEmployeeForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class EmployeeListView(LoginRequiredMixin, ListView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    template_name = "employees/employee_list.html"
    model = Employee
    context_object_name = "employees_list"
    
    # def get(self, request):
    #     employee_list = Employee.objects.all()``
    #     return render(request, "staff_app/employee_list.html", {
    #         "list": employee_list
    #     })

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


    # def get(self, request):
    #     form = NewEmployeeForm()
        
    #     return render(request, "staff_app/new_employee.html", {
    #         "form": form,
    #     })
    
    # def post(self, request):
    #     form = NewEmployeeForm(request.POST)

    #     if form.is_valid():
    #         success_text = "New employee added successfully!"
    #         form.save()
            
    #         return render(request, 'staff_app/new_employee.html', {
                
    #             "success": success_text,
    #             "form": form
    #         })
        
    #     else:   
    #         return render(request, "staff_app/new_employee.html", {
    #         "form": form
    #         })
       
class EditEmployeeView(LoginRequiredMixin, UpdateView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    model = Employee
    fields = "__all__"
    template_name = "employees/edit_employee.html"
    success_url = "/"

    # def get(self, request, id):
    #     edited_employee = Employee.objects.get(pk=id)
    #     form = NewEmployeeForm(instance=edited_employee)
    #     return render(request, "staff_app/edit_employee.html", {
    #     "form": form
    #     })
    
    # def post(self, request, id):
    #     form = NewEmployeeForm(instance=Employee.objects.get(pk=id))
    #     if form.is_valid():
    #         success_text = "Employee edited successfully!"
    #         form.save()
    #         return render(request, "staff_app/edit_employee.html", {
    #         "form": form,
    #         "success": success_text,
    #         "employee": edited_employee
    #         })
    #     else:
    #         pass

class DeleteEmployeeView(LoginRequiredMixin, DeleteView):
    login_url = 'user/login_user'
    redirect_field_name = '/'
    model=Employee
    success_url = "/"

# def DeleteEmployee(request, id):
#     if request.method == "POST":
#         deleted_employee = Employee.objects.get(id=id)
#         deleted_employee.delete()
#         return redirect("employee-list")

# class DepartmentListView(LoginRequiredMixin, ListView, pk=pk):
#     login_url = 'user/login_user'
#     redirect_field_name = '/'
#     template_name = "employees/management_list.html"
#     model = Employee
#     # context_object_name = "management_list"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         employees = Employee.objects.filter(department=1)
#         context["management"] = employees
#         return context

# class DepartmentListView(LoginRequiredMixin, View):
#     login_url = 'user/login_user'
#     redirect_field_name = '/'
   
#     def get(self, request, id):
#         department_employees = Employee.objects.filter(department=id)
#         return render(request, "employees/department_list.html", {
#             "department": department_employees
#         })

@login_required(login_url="/user/login_user")
def DepartmentList(request, department):
    if request.method == "GET":
        department_employees = Employee.objects.filter(department=department)
        return render(request, "employees/department_list.html", {
        "employees": department_employees,
        "department": department
        })


        #1 management 2 hr 3 accounting 5 logistics 6 warehouse