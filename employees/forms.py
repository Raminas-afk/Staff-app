from django import forms
from .models import Employee, Event
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        #exclude=["some_field"]             Example
        error_messages = {
                "required": "This field is required!",
                "max_length": "Name too long. Maximum 50 characters"
            }


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = "time"

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }
   

