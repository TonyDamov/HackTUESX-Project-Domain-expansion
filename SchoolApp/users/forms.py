from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','username','password1','password2']
        
        
class EditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','last_name','email','avatar']