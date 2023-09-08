from django.db import models

# Create your models here.


class Socio(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    correo = models.EmailField()


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()


class Deporte(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
