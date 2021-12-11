from rest_framework import serializers
from .models import Course,Classes,Student,Teacher,Subject,Results,Attendance,AttendanceReport,Appointment,Notifications

#course serializer

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'


#classes serializer
class ClassesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Classes
        fields = '__all__'


#student serializer
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'

        
#Teacher serializer
class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = '__all__'

#Subject serializer
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = '__all__'

#Results serializer
class  ResultsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Results
        fields = '__all__'



#Attendance serializer
class AttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attendance
        fields = '__all__'

#AttendanceReport serializer
class   AttendanceReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   AttendanceReport
        fields = '__all__'


#Appointment serializer
class  AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Appointment
        fields = '__all__'


#Notifications serializer
class  NotificationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notifications

        fields = '__all__'

