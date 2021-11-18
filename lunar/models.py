from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    course_code = models.IntegerField()
    course_name = models.CharField(max_length=200, null=True, blank=True)
    course_total = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.course_name

class Classes(models.Model):
    class_name = models.CharField(max_length=200, null=True, blank=True)
    class_code = models.IntegerField()
    class_assignments_written = models.CharField(max_length=200, null=True,blank=True)
    class_assignment_image = models.ImageField(null=True, blank=True,default='/placeholder.png')
    class_attendance = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.class_name




class Student(models.Model):
    student_id =models.IntegerField()
    student_group = models.CharField(max_length=200,null=True,blank=True)
    
    student_name = models.CharField(max_length=200,null=True,blank=True)
    
    student_class_code = models.IntegerField(null=True, blank=True,default=0)
    
    student_total =  models.IntegerField(null=True,blank=True,default=0)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.student_group

