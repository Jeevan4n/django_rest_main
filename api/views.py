from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
def studentsview(request):
    students={
        'id':2,
        'name':'chintu',
        'age':44
    }
    return HttpResponse(students)

def jeev(request):
    return HttpResponse("po ra hooka")
