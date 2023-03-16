from django.contrib import admin
from django.urls import path, include
from AppCoder import views

urlpatterns = [

    path('', views.inicio),
    path('cursos', views.cursos),
    path('profesores', views.profesores),
    path('cursos', views.cursos),
    path('cursos', views.cursos),



]