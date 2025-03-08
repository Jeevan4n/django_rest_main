from django.urls import path
from .views import home, student_list_create, student_detail

urlpatterns = [
    path('home/', home, name='home'),
    path('', student_list_create, name='student-list-create'),
    path('<int:pk>/', student_detail, name='student-detail'),
]