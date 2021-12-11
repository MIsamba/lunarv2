from django.shortcuts import render
from .models import Course, Classes, Student, Teacher,Subject,Results,Attendance,AttendanceReport,Appointment,Notifications
from .serializers import CourseSerializer,ClassesSerializer,StudentSerializer,TeacherSerializer,SubjectSerializer,ResultsSerializer,AttendanceSerializer,AttendanceReportSerializer,AppointmentSerializer,NotificationsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
  routes = [
    '/api/courses/'
    '/api/classes/'
    '/api/student/'
    '/api/teacher/'
    '/api/subject'
    '/api/results'
    '/api/attendance'
    '/api/AttendanceReport'
    '/api/Appointment'
    '/api/Notifications'

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
