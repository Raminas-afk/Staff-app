from django.db import models
# from django.core.validators import MinLengthValidator

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    DEPARTMENT_CHOICES = {
        ("Management", "Management"),
        ("HR", "HR"),
        ("Accounting", "Accounting"),
        ("Logistics", "Logistics"),
        ("Warehouse", "Warehouse"),
    }
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=20, default="Not assigned")
    salary = models.IntegerField(default=600)
    working_since = models.DateField()
    employee_picture = models.ImageField(upload_to="employee_pictures/", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




