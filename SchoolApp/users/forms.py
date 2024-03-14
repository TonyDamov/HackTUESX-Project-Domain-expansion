from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','username','password1','password2']