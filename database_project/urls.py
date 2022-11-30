# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employees import views


router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("employees.urls")),
    path('user/', include('django.contrib.auth.urls')),
    path('user/', include("authentication.urls")),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)         for file uploads, disabled for now

