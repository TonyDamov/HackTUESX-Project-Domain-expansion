from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('',views.home,name = 'Home-page'),
     path('Grades/',views.Grades,name = 'Your-Grades'),
     path('Login/',views.Log,name = 'Login-page')
]






urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)