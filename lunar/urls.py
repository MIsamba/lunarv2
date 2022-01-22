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
    path('student/',views.getStudent , name = "students"),
    path('teachers/',views.getStudent , name = "teachers"),
    path('subjects/',views.getSubject , name = "Subjects"),
    path('results/',views.getResults , name = "Results"),
    path('attendance/',views.getAttendance , name = "Attendance"),
    path('AttendanceReport/',views.getAttendanceReport , name = "AttendanceReport"),
    path('Appointment/',views.getAppointment , name = "Appointment"),
   

  ]