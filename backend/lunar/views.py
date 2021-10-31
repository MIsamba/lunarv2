from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.

import json
from .models import Course

def getRoutes(request):
    return JsonResponse("Hello", safe=False)

def getCouses(request, course_name):
    if request.method == "GET" :
        try:
          Course = course_name.objects.get(name = course_name)
          response = json.dump([{ 'Course Name': Course.course_name,'Number of Students': Course.course_total }])
        except:
          response = json.dumps([{'Error': 'No couses with that name'}])
   
    return HttpResponse(response,content_type='text/json')