from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name="employee-list"),
    path('new_employee', views.AddNewEmployeeView.as_view(), name="new-employee"),
    path('delete_employee/<int:pk>', views.DeleteEmployeeView.as_view(), name="delete-employee"),
    path('edit_employee/<int:pk>', views.EditEmployeeView.as_view(), name="edit-employee"),
    path('specific_employee/<int:pk>', views.SpecificEmployeeView.as_view(), name="specific-employee"),
    path('departments/<str:department>', views.department_list, name="department-list"),
    path('events', views.event_list, name='events'),
    path('new_event', views.AddNewEventView.as_view(), name='new-event'),
    path('edit_event/<int:pk>', views.EditEventView.as_view(), name="edit-event"),
    path('delete_event/<int:pk>', views.DeleteEventView.as_view(), name="delete-event"),
    path('specific_event/<int:pk>', views.SpecificEventView.as_view(), name="specific-event")
]
