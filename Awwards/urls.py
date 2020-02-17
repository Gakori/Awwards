"""Awwards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include

from django.contrib import admin

from wards import views

from django.contrib.auth import views as auth_views

from wards import views as wards_views

from django.conf.urls.static import static

from django.conf import settings

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', views.home, name='wards-home'),
    
    path('wards/', include('wards.urls')),
    
    path('', include('wards.urls')),
    
    path('register/', wards_views.register, name='register'),
    
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout' ),
    
    path('profile/', wards_views.profile, name='profile'),
    
    path('post/', views.PostList.as_view()),
    
    path('profile/', views.ProfileList.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
