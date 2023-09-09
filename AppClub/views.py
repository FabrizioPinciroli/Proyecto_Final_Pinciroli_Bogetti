from django.shortcuts import render
from django.http import HttpResponse
from AppClub.models import Socio
# Create your views here.


def socio(req, nombre, edad, correo):
    socio = Socio(nombre=nombre, edad=edad, correo=correo)
    socio.save()

    return HttpResponse(f"""
<p>Socio: {socio.nombre} edad: {socio.edad} correo: {socio.correo} Creado con éxito. """)


def listar_socios(req):
    lista = Socio.objects.all()

    return render(req, "lista_socios.html", {"lista_socios": lista})


def inicio(req):
    return render(req, "inicio.html")


def socio(req):
    return render(req, "socio.html")


def evento(req):
    return render(req, "evento.html")


def deporte(req):
    return render(req, "deporte.html")
