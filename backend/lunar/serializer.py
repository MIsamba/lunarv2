from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Course, Classes, Student


class CourseSerializer(serializers.ModelSerializer):
    course_code = serializers.SerializerMethodField(read_only=True)
    course_name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', '  course_code', ' course_name', 'course_total', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_course_name(self, obj):
        name = obj.course_name
        if name == '':
            name = obj.course_code

        return name