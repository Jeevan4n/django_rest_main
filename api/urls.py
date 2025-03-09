from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsview, name='student-view'),  # ✅ Removed ()
    path('jeev/',views.jeev,name='jeev'),
    path('student/<int:pk>/',views.student_detail,name='student-detail')
]
