from django.shortcuts import render,redirect
from .forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def registerPage(request):
    form=MyUserCreationForm()
    if request.method == 'POST':
        form=MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.save()
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request,'users/register.html',{'form':form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username_or_email=request.POST.get('username_or_email')
        password=request.POST.get('password')

        if '@' in username_or_email:
            kwargs={'email':username_or_email}
        
        else:
            kwargs={'username':username_or_email}
        user= authenticate(request,**kwargs,password=password)

        if user is not None:
            login(request,user)
        else:
            messages.error(request, 'User does not exist')
    return render(request,'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home-page')
