from django.contrib import admin
from .models import Employee, Event, Departments
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ('department',)
    list_display = ('full_name','salary', 'working_since')
    



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Event)
admin.site.register(Departments)