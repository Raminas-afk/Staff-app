from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm
from django.urls import reverse
# Create your views here.

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'authenticate/login.html', {
            "form": form
        })
    
    def post(self,request):
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            login_message = "You logged in successfuly!"
            return redirect(reverse('employee-list'), {
                "message": login_message
            })
        else:
            login_message = "Something went wrong, check your login details"
            form = LoginForm()
            return render(request, 'authenticate/login.html',{
                "message": login_message,
                "form": form
                })

class LogoutView(View):
    def get(self, request):
        logout(request)
        form = LoginForm
        logout_message = "Logged out successfuly"
        return render(request, 'authenticate/login.html',{
                "message": logout_message,
                "form": form
        })
