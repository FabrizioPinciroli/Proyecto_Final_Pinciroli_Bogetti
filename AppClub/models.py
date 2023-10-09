from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Deporte(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()
    partido = models.ForeignKey(Deporte, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"
