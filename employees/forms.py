from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        #exclude=["some_field"]             Example
        error_messages = {
                "required": "This field is required!",
                "max_length": "Name too long. Maximum 50 characters"
            }
        

# class NewUserForm(UserCreationForm):              Currently not needed!
#     user_name = forms.CharField(max_length=20)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ("user_name","email")
    
#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.user_name = self.cleaned_data['user_name']
#         user.email = self.cleaned_data['email']
#         user.password = self.cleaned_data['password']
#         if commit:
#             user.save()
#         return user