from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from students.models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def studentsview(request):
    if request.method == 'GET':
        # Fetch all students
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    #handles get,put,delete for a single student
    student=get_object_or_404(Student,pk=pk)
    if(request.method=='GET'):
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif(request.method=='PUT'):
        serializer=StudentSerializer(student,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='DELETE'):
        student.delete()
        return Response({"message":"student deleted successfully"},status=status.HTTP_204_NO_CONTENT)

def jeev(request):
    return HttpResponse("hello world")
    

