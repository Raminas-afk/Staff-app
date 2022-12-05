from django.db import models
# from django.core.validators import MinLengthValidator

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    # DEPARTMENT_CHOICES = {
    #     ("Management", "Management"),
    #     ("HR", "HR"),
    #     ("Accounting", "Accounting"),
    #     ("Logistics", "Logistics"),
    #     ("Warehouse", "Warehouse"),
    # }
    department = models.ForeignKey("Departments", on_delete=models.PROTECT, default=None)
    salary = models.IntegerField(default=600)
    working_since = models.DateField()
    employee_picture = models.ImageField(upload_to="employee_pictures/", null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.first_name

class Departments(models.Model):
    name = models.CharField(max_length=50)
    employees = models.ManyToManyField(Employee, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    attending_department = models.ForeignKey(Departments, on_delete=models.CASCADE, default="Not specified")
    # attending_extra = models.ManyToManyField(Employee, default="Not specified", blank=True)  ?? Shows up as employees.Employee.None 
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    
    def __str__(self):
        return self.name