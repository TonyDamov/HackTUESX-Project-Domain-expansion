from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views 
from . import views as user_views

urlpatterns = [
   #path('',user_views.,name = 'login-page'),
   path('register/',views.registerPage,name = 'register-page'),
]