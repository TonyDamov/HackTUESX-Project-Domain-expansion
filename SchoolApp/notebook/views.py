from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Grade,Material, Subject
from django.contrib.auth.decorators import login_required
from users.forms import User
from .forms import MaterialForm
# Create your views here.

@login_required(login_url='login-page')
def homeProfile(request):
    if not request.user.is_authenticated:
        return redirect('login-page')
    else:
     return render(request,'notebook/homepage.html')

@login_required(login_url='login-page')
def Materials(request):
    materials = Material.objects.all()
    return render(request,'notebook/materials.html',{'materials':materials})

def Grades(request):
    
    if request.user.role == 'Student':
        grades = Grade.objects.filter(user=request.user).values('subject__title', 'grade')
        subjects = Subject.objects.filter(student=request.user)
    else:
        grades = []
        subjects = Subject.objects.filter(teacher=request.user)
        for subject in subjects:
            grades.append(Grade.objects.filter(subject=subject))
<<<<<<< HEAD
    return render(request,'notebook/grades.html',{'grades' : grades, 'subjects' : subjects})

def createMaterial(request):
    if request.user.role == 'Teacher':
        form=MaterialForm()
        if request.method == 'POST':
            form=MaterialForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home-page')
    else:
        return redirect('home-page')
    return render(request,'notebook/materials_create.html',{'form':form})
=======
    return render(request,'notebook/grades.html',{'grades' : grades, 'subjects' : subjects})
>>>>>>> 8f7209519379c68051b63ea309c0a25d19982a4c
