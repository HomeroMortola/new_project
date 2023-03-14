from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def curso(self):
    curso = curso(nombre = 'desarroyo')
    curso.save()

    documento = f'-->Curso: {curso.nombre}'

    return HttpResponse(documento)


