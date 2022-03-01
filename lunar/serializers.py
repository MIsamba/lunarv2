from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import UniqueTogetherValidator


from .models import  Hero,Posts,Assignments,Documents, User,Course,Session,Student,Students,Teacher,Subject,Results,Attendance,AttendanceReport,Appointment


#User serializer

#class UserSerializer(serializers.ModelSerializer):
   # name = serializers.SerializerMethodField(read_only=True)
 #   class Meta:
  #      model = User
   #     fields = ['id','username','email']
   


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['id', 'password']
            )
        ]



class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
  
    class Meta:
        model = User
        fields = '__all__'
        #['id','_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


#hero
class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'
#course serializer

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'


#Session serializer
class SessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Session
        fields = '__all__'


#student serializer
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
#student serializer

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
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



#Posts serializer
class  PostsSerializer(serializers.ModelSerializer):
    
    avater = serializers.ImageField(use_url = True)
    #avater = serializers.SerializerMethodField('get_avater')

    class Meta:
        model = Posts
        fields = '__all__'

    #def get_avater(self, obj):
     # return obj.avater.url


#Documents serializer
class  DocumentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Documents
        fields = '__all__'

#Assignments serializer
class  AssignmentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Assignments
        fields = '__all__'

