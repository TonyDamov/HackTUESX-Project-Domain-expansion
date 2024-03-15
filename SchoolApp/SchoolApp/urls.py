"""
URL configuration for SchoolApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from notebook import views as note_views
from users import views as user_views
from django.views.generic import ListView, DetailView, DeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('materials/',note_views.Materials,name = 'material-page'),
    path('grades/',note_views.Grades,name = 'your-grades'),
    path('home/',note_views.homeProfile,name = 'home-page'),
    path('',user_views.loginPage,name = 'login-page'),
    path('register/',user_views.registerPage,name = 'register-page'),
    path('logout/',user_views.logoutUser,name = "logout-page"),
    path('profile/',user_views.editUser,name = 'profile-page'),
    path('create-material/',note_views.createMaterial,name = 'create-material')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)