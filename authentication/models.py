from django.contrib.auth.models import AbstractUser
from django.db import models
from AppClub.models import Evento, Deporte


class Perfil(AbstractUser):
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True)
    domicilio = models.CharField(max_length=25, null=True)
    evento = models.OneToOneField(
        Evento, on_delete=models.SET_NULL, blank=True, null=True
    )
    deporte = models.OneToOneField(
        Deporte, on_delete=models.SET_NULL, blank=True, null=True
    )
    avatar = models.ImageField(upload_to="avatares/", null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nombre", "apellido"]

    def __str__(self):
        return f"{self.username}"
