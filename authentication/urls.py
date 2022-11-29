from django.urls import path
from . import views

urlpatterns = [
    path("login_user", views.LoginView.as_view(), name="login"),
    path("logout_user", views.LogoutView.as_view(), name="logout")
]