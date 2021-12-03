from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from kineticapi.views import register_user, login_user
"""kinetic URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

urlpatterns = [
path('register', register_user),
path('login', login_user),
path('api-auth', include('rest_framework.urls',
namespace='rest_framework')),
path('admin/', admin.site.urls),
]