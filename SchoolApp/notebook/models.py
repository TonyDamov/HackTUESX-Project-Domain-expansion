from django.db import models
from users.models import User
from django.utils import timezone
from django.contrib.auth.models import Group
# Create your models here.

class Material(models.Model) :
    file = models.FileField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(User, models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='materials')
    def __str__(self) -> str :
        return f'{self.user} - {self.title}'
    
    @property
    def image_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
        else:
            return ""
    
class Subject(models.Model):
    teacher = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=128, null=False, blank=False)
    def __str__(self) -> str :
        return f'{self.title} - {self.teacher}'
    
class Grade(models.Model) :
    grade = models.DecimalField(null=False, blank=False, decimal_places = 2, max_digits = 3)
    user = models.ForeignKey(User, models.CASCADE, related_name='student')
    subject = models.ForeignKey(Subject, models.CASCADE)
    teacher = models.ForeignKey(User, models.CASCADE, related_name='teacher')
    def __str__(self) -> str :
        return f'{self.grade} - {self.user}'
