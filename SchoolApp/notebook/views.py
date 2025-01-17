from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Grade,Material, Subject
from django.contrib.auth.decorators import login_required
from users.forms import User
from .forms import MaterialForm,GradeForm,EditGradeForm

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
                file=request.FILES['file'],
            )
            return redirect('material-page')

    else:
        return redirect('home-page')
    return render(request,'notebook/materials_create.html',{'form':form})

@login_required(login_url='login-page')
def updateMaterial(request, pk):
    if request.user.role == 'Teacher':
        material = Material.objects.get(id=pk)
        if request.user != material.user:
            return HttpResponse('You are not allowed here!')

        if request.method == 'POST':
            form = MaterialForm(request.POST, request.FILES, instance=material)
            if form.is_valid():
                form.save()
                return redirect('material-page')
        else:
            form = MaterialForm(instance=material)

        return render(request, 'notebook/materials_update.html', {'form': form})
    else:
        return redirect('home-page')

@login_required(login_url='login-page')
def deleteMaterial(request, pk):
    if request.user.role == 'Teacher':
        material = Material.objects.get(id=pk)
        if request.user != material.user:
            return HttpResponse('You are not allowed here!')

        if request.method == 'POST':
            material.delete()
            return redirect('material-page')

        return render(request, 'notebook/materials_delete.html',{'material':material})
    else:
        return redirect('home-page')

def createGrade(request):
    if request.user.role == 'Teacher':
        form=GradeForm()
        if request.method == 'POST':
            form=GradeForm(request.POST)
            if form.is_valid():
                grade=form.save(commit=False)
                grade.teacher=request.user
                grade.save()
                return redirect('your-grades')
    else:
        return redirect('home-page')
    students=User.objects.filter(role='Student')
    return render(request,'notebook/grades_create.html',{'form':form, 'students':students})

def editGrade(request,pk):
   def updateGrades(request, user_id):
    grades = Grade.objects.filter(user_id=user_id)
    
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            for grade in grades:
                grade.grade = form.cleaned_data['grade']
                grade.save()
            return redirect('grades')
    else:
        form = GradeForm(initial={'grade': grades.first().grade}) if grades.exists() else GradeForm()
    
    return render(request, 'notebook/update_grades.html', {'form': form})



