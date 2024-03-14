from django.contrib import admin
from .models import Grade
# Register your models here.

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin) :
    list_display = ('grade', 'user')