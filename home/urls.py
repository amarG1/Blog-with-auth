from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    # path('', views.index, name="home"),
    path('login/', views.loginuser, name="login"),
    path('register/', views.reg, name="register"),
    path('logout/', views.logoutuser, name="logout"),
]
