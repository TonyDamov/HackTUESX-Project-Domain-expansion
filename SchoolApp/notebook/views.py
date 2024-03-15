from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Grade,Material
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login-page')
def home(request):
    if not request.user.is_authenticated:
        return redirect('login-page')
    return render(request,'notebook/homepage.html')

@login_required(login_url='login-page')
def Materials(request):
    materials = Material.objects.all()
    return render(request,'notebook/materials.html',{'materials':materials})

def Grades(request):
    grades = Grade.objects.all()
    

    return render(request,'notebook/grades.html',{'grades' : grades})
