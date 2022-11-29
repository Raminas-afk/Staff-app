from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name="employee-list"),
    path('new_employee', views.AddNewEmployeeView.as_view(), name="new-employee"),
    path('delete_employee/<int:pk>', views.DeleteEmployeeView.as_view(), name="delete-employee"),
    path('edit_employee/<int:pk>', views.EditEmployeeView.as_view(), name="edit-employee"),
    path('specific_employee/<int:pk>', views.SpecificEmployeeView.as_view(), name="specific-employee"),
    path('departments/<str:department>', views.DepartmentList, name="department-list")
]
