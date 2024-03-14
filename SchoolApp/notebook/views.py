from django.shortcuts import render
from django.http import HttpResponse
from .models import Grade,Material

# Create your views here.


def home(request):
    return render(request,'notebook/homepage.html')


def Materials(request):
    materials = Material.objects.all()
    return render(request,'notebook/materials-s.html',{'materials':materials})


def Grades(request):
    grades = Grade.objects.all()
    

    return render(request,'notebook/grades.html',{'grades' : grades})
