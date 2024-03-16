from django.shortcuts import render,redirect
from .forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import User,EditForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.urls import reverse

# Create your views here.
@login_required(login_url='login-page')
def userProfile(request, pk):
    user=User.objects.get(id=pk)
    return render(request,'users/profile.html',{'user': user })


def registerPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        has_atleast_eight_characters = False
        has_atleast_one_digit = any(map(str.isdigit, password))
        has_atleast_one_upper = any(map(str.isupper, password))
        has_atleast_one_lower = any(map(str.islower, password))
        has_no_forbidden = False

        if len(str(password)) >= 8:
            has_atleast_eight_characters = True

        if not str(password).__contains__('!') or not str(password).__contains__('$') or not str(password).__contains__('#') or not str(password).__contains__('%'):
            has_no_forbidden = True

        if not username:
            messages.error(request, "The 'Username' field can not be empty!")
            return render(request, "users/register.html")

        if not email:
            messages.error(request, "The 'Email' field can not be empty!")
            return render(request, "users/register.html")

        if not password:
            messages.error(request, "The 'Password' field can not be empty!")
            return render(request, "users/register.html")

        if not confirm_password:
            messages.error(request, "The 'Confirm password' field can not be empty!")
            return render(request, "users/register.html")

        if password != confirm_password:
            messages.error(request, "Passwords must match!")
            return render(request, "users/register.html")

        if not has_atleast_eight_characters:
            messages.error(request, "The password can not contain less than 8 characters!")
            return render(request, "users/register.html")

        if not has_atleast_one_digit:
            messages.error(request, "The password should contains atleast one digit!")
            return render(request, "users/register.html")

        if not has_atleast_one_upper:
            messages.error(request, "The password should contains atleast one upper character!")
            return render(request, "users/register.html")

        if not has_atleast_one_lower:
            messages.error(request, "The password should contains atleast one lower character!")
            return render(request, "users/register.html")

        if not has_no_forbidden:
            messages.error(request, "The password should not contains '!', '$', '#' or '%'!")
            return render(request, "users/register.html")

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "You have signed up successfully!")
            return HttpResponseRedirect(reverse("home-page"))
        except IntegrityError:
            messages.error(request, "Username already taken.")
            return render(request, "users/register.html")
    else:
        return render(request, "users/register.html")


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
            return redirect('home-page')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login-page')


@login_required(login_url='login')
def editUser(request):
    user = request.user
    form =EditForm(instance=user)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile-page', pk=user.id)

    return render(request, 'users/edituser.html', {'form': form})

