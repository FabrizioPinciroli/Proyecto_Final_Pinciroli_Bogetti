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
    imagen = models.ImageField(upload_to="noticias", null=True, blank=True)
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


opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"],
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensajes = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"
