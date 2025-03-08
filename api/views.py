from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import  api_view
from students.models import Student
from .serializers import StudentSerializer


@api_view(['GET','POST'])
def studentsview(request):
    if(request.method=='GET'):
        #get all the a from the student table
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
         serializer=StudentSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    
def jeev(request):
    return HttpResponse("po ra hooka")
