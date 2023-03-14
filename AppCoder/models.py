from django.db import models

# Create your models here.

class curso(models.Model):
    nombre=models.CharField(max_length=40)

class estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)

class profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    profecion=models.CharField(max_length=40)

class entregabel(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
