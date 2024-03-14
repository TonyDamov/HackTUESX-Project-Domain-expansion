from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'notebook/base.html')

def Grades(request):
    return render(request,'')
