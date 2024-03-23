from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="landingpage"),
    path('login', views.home, name="landingpage"),
    path('home', views.index, name="home"),
    path('form', views.post, name="form"),
    path('post/', views.post, name="post"),
    path('register', views.register, name="register"),
    path('logout/', views.logOut, name="logout"),
]
