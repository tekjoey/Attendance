from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Student, Attendance
# Create your views here.

def index(request):
    template = loader.get_template('attendance/index.html')
    return HttpResponse(template.render({}, request))

def teacher(request):
    print(request)
    return HttpResponse("Hello, world. You're at the database / teacher index.")

def student(request, last_name):
    template = loader.get_template('attendance/student_view.html')
    return HttpResponse(template.render({'last_name': last_name}, request))