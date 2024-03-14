from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from users.views import registerPage as auth_views


urlpatterns = [
     #path('',,name = 'login'),
     path('materials/',views.Material,name = 'Material-page'),
     path('register/',auth_views,name = 'register-page'),
     path('grades/',views.Grades,name = 'your-grades'),
     path('home/',views.home,name = 'home-page')
  ]






urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)