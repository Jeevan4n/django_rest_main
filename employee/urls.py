from django.urls import path
from . import views

urlpatterns = [
   path('varun/',views.varun,name='my-varun')
]