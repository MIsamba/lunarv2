from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .models import Posts,Documents, User,Course, Session, Students,Student, Teacher,Subject,Results,Attendance,AttendanceReport,Appointment,Documents,Assignments
from .serializers import UserSerializer, UserSerializerWithToken,CourseSerializer,SessionSerializer,StudentSerializer,StudentsSerializer,TeacherSerializer,SubjectSerializer,ResultsSerializer,AttendanceSerializer,PostsSerializer,AssignmentsSerializer,DocumentsSerializer,AppointmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.


@api_view(['POST'])
def registerUser(request):
    data = request.data
    user = User.objects.create(
        #first_name = data['name'],
        username=data['username'],
        #email=data['email'],
        #phoneNumber=data['phoneNumber'],
        #idnumber=data['idnumber'],
        #college=data['college'],
        #course=data['course'],
        #year_of_enrollment=data['year_of_enrollment'],
        #profile_photo=data['profile_photo'],
        #gender=data['gender'],
        #password=make_password(data['password'])
    )

    serializer = UserSerializerWithToken(user, many=True)
    return Response(serializer.data)

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
def getSession(request):
    session = Session.objects.all()
    serializer = SessionSerializer(session, many =True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudent(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many =True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def getStudents(request):
    students = Students.objects.all()
    serializer = StudentsSerializer(students, many =True)
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
def getPosts(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getDocuments(request):
    documents = Documents.objects.all()
    serializer = DocumentsSerializer(documents, many =True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def getAssignments(request):
    assignments = Assignments.objects.all()
    serializer = AssignmentsSerializer(assignments, many =True)
    return Response(serializer.data)
