from django.db import models


class Deporte(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    categoria = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre}"


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    fecha = models.DateField()
    tema = models.CharField(max_length=100)
    desarrollo = models.TextField(max_length=300)
    imagen = models.ImageField(upload_to="avatares/", null=True, blank=True)
    pie_de_foto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo}"


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"
