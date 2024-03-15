from django.contrib import admin
from .models import Grade, Material, Subject
# Register your models here.

#@admin.register(Grade)
#class GradeAdmin(admin.ModelAdmin) :
    #list_display = ('grade', 'user')
admin.site.register(Grade)
admin.site.register(Material)
admin.site.register(Subject)