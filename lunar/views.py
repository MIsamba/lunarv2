from django.shortcuts import render
from rest_framework import serializers
from .models import User,Course, Classes, Student, Teacher,Subject,Results,Attendance,AttendanceReport,Appointment,Notifications
from .serializers import UserSerializer, UserSerializerWithToken,CourseSerializer,ClassesSerializer,StudentSerializer,TeacherSerializer,SubjectSerializer,ResultsSerializer,AttendanceSerializer,AttendanceReportSerializer,AppointmentSerializer,NotificationsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   def validate(self, attrs):
       data = super().validate(attrs)

       data['username'] = self.user.username
       data['email'] = self.user.email
       return data
        
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.

@api_view(['POST'])
def registerUser(request):
    data = request.data

    user = User.objects.create(
        first_name = data['name'],
        username=data['email'],
        email=data['email'],
        phoneNumber=data['phoneNumber'],
        Id_number=data['Id_number'],
        college=data['college'],
        course=data['course'],
        year_of_enrollment=data['year_of_enrollment'],
        profile_photo=data['profile_photo'],
        gender=data['gender'],
        password=make_password(data['password']),
       
    )
    serializer = UserSerializerWithToken(user, many=False)
    return Response('serializer.data')

@api_view(['GET'])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many =False)
    return Response(serializer.data)



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

@api_view(['GET'])
def getTeacher(request):
    teacher = Teacher.objects.all()
    serializer = TeacherSerializer(teacher, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getSubject(request):
    subject = Subject.objects.all()
    serializer = SubjectSerializer(subject, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getResults(request):
    results = Results.objects.all()
    serializer = ResultsSerializer(results, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getAttendance(request):
    attendance = Attendance.objects.all()
    serializer = AttendanceSerializer(attendance, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getAttendanceReport(request):
    attendanceReport = AttendanceReport.objects.all()
    serializer = AttendanceSerializer(attendanceReport, many =True)
    return Response(serializer.data)

@api_view(['GET'])
def getAppointment(request):
    appointment = Appointment.objects.all()
    serializer = AppointmentSerializer(appointment, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getNotifications(request):
    notifications = Notifications.objects.all()
    serializer = NotificationsSerializer(notifications, many =True)
    return Response(serializer.data)

