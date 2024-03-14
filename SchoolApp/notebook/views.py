from django.shortcuts import render
from django.http import HttpResponse
from .models import Grade
# Create your views here.


def home(request):
    return render(request,'notebook/login-page.html')

def Grades(request):
    grades = Grade.objects.all()
    

    return render(request,'notebook/grades.html',{'grades' : grades})
