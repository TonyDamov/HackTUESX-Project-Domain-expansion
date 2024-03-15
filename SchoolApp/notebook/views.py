from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Grade,Material
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login-page')
def home(request):
    return render(request,'notebook/homepage.html')

@login_required(login_url='login-page')
def Materials(request):
    materials = Material.objects.all()
    return render(request,'notebook/materials.html',{'materials':materials})
"""
class MaterialsListView(ListView):
    model = Material
    template_name = 'notebook/materials.html'
    context_object_name = 'materials'
    ordering = ['-date_posted']

class MaterialsDetailView(DetailView):
    model = Material
    context_object_name = 'materials'
"""
@login_required(login_url='login-page')
def Grades(request):
    grades = Grade.objects.all()
    

    return render(request,'notebook/grades.html',{'grades' : grades})
