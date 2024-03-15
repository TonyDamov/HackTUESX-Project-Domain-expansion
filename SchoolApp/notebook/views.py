from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Grade,Material, Subject
from django.contrib.auth.decorators import login_required
from users.forms import User
# Create your views here.

@login_required(login_url='login-page')
def homeProfile(request,pk):
    if not request.user.is_authenticated:
        return redirect('login-page')
    else:
     user = User.objects.get(pk = id)
    return render(request,'notebook/homepage.html')

@login_required(login_url='login-page')
def Materials(request):
    materials = Material.objects.all()
    return render(request,'notebook/materials.html',{'materials':materials})

def Grades(request):
    
    if request.user.role == 'Student':
        grades = Grade.objects.filter(user=request.user)
    else :
        grades = []
        subjects = Subject.objects.filter(teacher=request.user)
        for subject in subjects:
            grades.append(Grade.objects.filter(subject=subject))
    return render(request,'notebook/grades.html',{'grades' : grades, 'subjects' : subjects})
