from django.urls import path
from . import views


urlpatterns = [
     path('',views.home,name = 'Home-page'),
     path('Grades/',views.Grades,name = 'Your-Grades')
]