from django.urls import path
from . import views

#url path
urlpatterns = [ 

    path('', views.getRoutes, name="routes"),
    path('courses/',views.getCourses , name = "courses"),
    path('classes/',views.getClasses , name = "classes"),
    path('student/',views.getStudent , name = "courses"),
  ]