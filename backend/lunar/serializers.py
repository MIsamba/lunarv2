from rest_framework import  serializers
from .models import Course, Classes, Student

#course serializer
class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields ='__all__'


#classes serializer
class ClassesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Classes
        fields ='__all__'


#student serializer
class  StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Student
        fields ='__all__'