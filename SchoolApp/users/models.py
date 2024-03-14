from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    last_name=models.CharField(max_length=100, null=True)
    email=models.EmailField(unique=True)
    avatar=models.ImageField(default='default.jpg')

# Create your models here.
