from django.shortcuts import render
from django.http import HttpResponse
from AppClub.models import Socio
# Create your views here.


def socios(req, nombre, edad, correo):
    socios = Socio(nombre=nombre, edad=edad, correo=correo)
    socios.save()

    return HttpResponse(f"""
<p>Socio: {socios.nombre} edad: {socios.edad} correo: {socios.correo} Creado con éxito. """)


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


def socioFormulario(req):
    if req.method == 'POST':
        socio = Socio(nombre=req.POST["nombre"], apellido=req.POST["apellido"],
                      edad=req.POST["edad"], correo=req.POST["correo"])
        socio.save()
        return render(req, "inicio.html")

    else:
        return render(req, "socioFormulario.html")
