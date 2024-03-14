from django.shortcuts import render
from django.http import HttpResponse
from .models import Grade,Material

# Create your views here.


def home(request):
    return render(request,'notebook/')


def Materials(request):
    material = Material.objects.all()
    
    return render(request,'notebook/',{'materials':material})


def Grades(request):
    grades = Grade.objects.all()
    

    return render(request,'notebook/grades.html',{'grades' : grades})
