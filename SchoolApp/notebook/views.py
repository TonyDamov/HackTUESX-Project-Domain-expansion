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
    materials = Material.objects.filter(groups__in=request.user.groups.all())
    return render(request,'notebook/materials.html',{'materials':materials})

@login_required(login_url='login-page')
def Grades(request):
        
    grades = []
    data = {}
    subjects = []
    print(request.user.role)
    if request.user.role == 'Student':
        grades = Grade.objects.filter(user=request.user)
        print(grades)
    
    else:
        data = {}
        subjects = Subject.objects.filter(teacher=request.user).order_by('title')
        
        for subject in subjects:
            grades = Grade.objects.filter(subject=subject)
            student_grades = {}
            for grade in grades:
                student_name = grade.user.username
                if student_name not in student_grades :
                    student_grades[student_name] = []
                student_grades[student_name].append(grade.grade)
            data[subject.title] = student_grades
        print(data)
    return render(request,'notebook/grades.html',{'grades' : grades, 'subjects' : subjects, 'data' : data}) 


@login_required(login_url='login-page')
def createMaterial(request):
    if request.user.role == 'Teacher':
        form=MaterialForm()
        if request.method == 'POST':
            Material.objects.create(
                user=request.user,
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                file=request.FILES['file']
            )

    else:
        return redirect('home-page')
    return render(request,'notebook/materials_create.html',{'form':form})

@login_required(login_url='login-page')
def updateMaterial(request, pk):
    if request.user.role == 'Teacher':
        material = Material.objects.get(id=pk)
        form = MaterialForm(instance=material)
        if request.user != material.user:
            return HttpResponse('You are not allowed here!')
        if request.method == 'POST':
            material.title = request.POST.get('title')
            material.description = request.POST.get('description')
            if 'file' in request.FILES:
                material.file = request.FILES['file']
            material.save()
            return redirect('material-page')
    else:
        return redirect('home-page')
    return render(request, 'notebook/materials_update.html', {'form': form})

