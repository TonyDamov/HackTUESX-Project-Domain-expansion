from django.shortcuts import render,redirect
from .forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def registerPage(request):
    form=MyUserCreationForm()
    if request.method == 'POST':
        form=MyUserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            #user.save()
            user=form.save()
            user.save()
            login(request, user)

            #redirect('home-page')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request,'users/register.html',{'form':form})


