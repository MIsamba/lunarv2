from django.shortcuts import render
from .models import Course,Classes,Student
from .serializers import CourseSerializer,ClassesSerializer,StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
  routes = [
    '/api/courses/'
    '/api/classes/'
    '/api/student/'

  ]
  return Response (routes)


@api_view(['GET'])
def getCourses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getClasses(request):
    classes = Classes.objects.all()
    serializer = ClassesSerializer(classes, many =True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudent(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many =True)
    return Response(serializer.data)
