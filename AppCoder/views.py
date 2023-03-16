from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.
'''
def curso(self):
    curso = Curso(nombre = 'desarroyo' , camada =1234 )
    curso.save()

    documento = f'-->Curso: {curso.nombre},{curso.camada}'

    return HttpResponse(documento)
'''

def inicio(recuest):
    return render(recuest, 'AppCoder/inicio.html')

def cursos(recuest):
    return render(recuest, 'AppCoder/cursos.html')

def profesores(recuest):
    return render(recuest, 'AppCoder/profesores.html')

def estudiantes(recuest):
    return render(recuest, 'AppCoder/estudiantes.html')

def entregables(recuest):
    return render(recuest, 'AppCoder/entregables.html')

