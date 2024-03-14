from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Grade(models.Model) :
    grade = models.DecimalField(null=False, blank=False, decimal_places = 2, max_digits = 3)
    user = models.ForeignKey(User, models.CASCADE)
    def __str__(self) -> str:
        return str(self.grade)