from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,'notebook/')

def Grades(request):
    return render(request,'notebook/grades.html')

def Log(request):
    return render(request,'notebook/login.html')
    
    
