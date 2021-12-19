from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Course model
class Course(models.Model):
    course_code = models.IntegerField()
    course_name = models.CharField(max_length=200, null=True, blank=True)
    course_total = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.course_name
#Classes model
class Classes(models.Model):
    class_name = models.CharField(max_length=200, null=True, blank=True)
    class_code = models.IntegerField()
    class_assignments_written = models.CharField(max_length=200, null=True,blank=True)
    class_assignment_image = models.ImageField(null=True, blank=True,default='/placeholder.png')
    class_attendance = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.class_name



#Student model
class Student(models.Model):
    student_id =models.IntegerField()
    student_group = models.CharField(max_length=200,null=True,blank=True)
    
    student_name = models.CharField(max_length=200,null=True,blank=True)
    
    student_class_code = models.IntegerField(null=True, blank=True,default=0)
    
    student_total =  models.IntegerField(null=True,blank=True,default=0)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.student_group

#Teacher model
class Teacher(models.Model):
    Teacher_id =models.IntegerField()
    Teacher_name = models.CharField(max_length=200,null=True,blank=True)
    Teacher_subject = models.CharField(max_length=200, null=True, blank = True)
    Teacher_total =  models.IntegerField(null=True,blank=True,default=0)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.Teacher_name

 #Subject model
class Subject(models.Model):
    Subject_id =models.IntegerField()
    Subject_name = models.CharField(max_length=200,null=True,blank=True)
    Subject_Teacher = models.CharField(max_length=200, null=True, blank = True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.Subject_name

#Results model
class Results(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
    subject_assignment_marks = models.FloatField(default=0)
    id = models.AutoField(primary_key=True,editable=False)
    objects = models.Manager()

    def __str__(self):
        return self.subject_assignment_marks


 #Attendance model  
class Attendance(models.Model):
    Subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    Attendance_date = models.DateField()
    Student_id =models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.Attendance_date

#Attendance Report model
class AttendanceReport(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    Attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.Attendance_id

#Appointment model
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    appointment_date = models.CharField(max_length=255)
    appointment_message = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.appointment_message

#Notifications model
class Notifications(models.Model):
    Course_name = models.CharField(max_length=200,null=True,blank=True)
    Tutor = models.CharField(max_length=200,null=True,blank=True)
    Course_Code = models.IntegerField()
    Venue = models.CharField(max_length=200,null=True,blank=True)

    Time=models.IntegerField()

    def __str__(self):
        return self.Course_name
