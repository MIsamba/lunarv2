from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
)
#url path
urlpatterns = [ 
    path('api/users/login/', TokenObtainPairView.as_view(),
     name='token_obtain_pair'),

    path('', views.getRoutes, name="routes"),
    path('courses/',views.getCourses , name = "courses"),
    path('classes/',views.getClasses , name = "classes"),
    path('student/',views.getStudent , name = "students"),
    path('teachers/',views.getStudent , name = "teachers"),
    path('subjects/',views.getSubject , name = "Subjects"),
    path('results/',views.getResults , name = "Results"),
    path('attendance/',views.getAttendance , name = "Attendance"),
    path('AttendanceReport/',views.getAttendanceReport , name = "AttendanceReport"),
    path('Appointment/',views.getAppointment , name = "Appointment"),
    path('Notifications/',views.getNotifications , name = "Notifications"),


  ]