from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('api/', include('api.urls')),
    path('employee/',include('employee.urls')),
]