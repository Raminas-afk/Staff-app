from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ('department',)
    list_display = ('first_name', 'last_name', 'salary', 'working_since')
    



admin.site.register(Employee, EmployeeAdmin)
