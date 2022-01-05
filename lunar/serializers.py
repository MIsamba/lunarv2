from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User,Course,Classes,Student,Teacher,Subject,Results,Attendance,AttendanceReport,Appointment,Notification

#User serializer

class UserSerializer(serializers.ModelSerializer):
   # name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email']
    
'''    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name 
'''
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
  
    class Meta:
        model = User
        fields = '__all__'
        #['id','_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
       


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
class  NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        fields = '__all__'

