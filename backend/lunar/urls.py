from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
)
#url path
urlpatterns = [ 
    path('api/users/login/', views.MyTokenObtainPairView.as_view(),
     name='token_obtain_pair'),

    path('users/profile/',views.getUserProfile , name = "users-profile"),
    path('users/register/',views.registerUser, name = "users-register"),
    
    path('courses/',views.getCourses , name = "courses"),
    path('session/',views.getSession , name = "session"),
    path('student/',views.getStudent , name = "student"),
    path('students/',views.getStudents , name = "students"),
    path('teachers/',views.getStudent , name = "teachers"),
    path('subjects/',views.getSubject , name = "Subjects"),
    path('results/',views.getResults , name = "Results"),
    path('attendance/',views.getAttendance , name = "Attendance"),
    path('attendanceReport/',views.getAttendanceReport , name = "AttendanceReport"),
    path('appointment/',views.getAppointment , name = "Appointment"),
    path('documents/',views.getDocuments , name = "Documents"),
    path('assignments/',views.getAssignments , name = "Assignments"),
    path('posts/',views.getPosts , name = "Posts"),
    
   

  ]