from django.db import models
from users.models import User



class Grade(models.Model) :
    grade = models.DecimalField(null=False, blank=False, decimal_places = 2, max_digits = 3)
    user = models.ForeignKey(User, models.CASCADE)
    def __str__(self) -> str :
        return f'{self.grade} - {self.user}'

class Material(models.Model) :
    file = models.FileField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(User, models.CASCADE)
    group = models.ManyToManyField(User, related_name='materials')
    def __str__(self) -> str :
        return f'{self.user} - {self.title}'
    
