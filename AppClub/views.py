from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from AppClub.models import *
from .forms import *
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
        miFormulario = SocioFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            socio = Socio(nombre=data["nombre"], apellido=data["apellido"],
                          edad=data["edad"], correo=data["correo"])
            socio.save()

            return render(req, "inicio.html")

    else:
        miFormulario = SocioFormulario()
        return render(req, "socioFormulario.html", {"miFormulario": miFormulario})


def busquedaApellido(req):
    return render(req, "busquedaApellido.html")


def buscar1(req: HttpRequest):

    if req.GET['Apellido']:
        apellido = req.GET['Apellido']
        socios = Socio.objects.filter(apellido=apellido)
        return render(req, "resultadoBusqueda1.html", {"socios": socios})
    else:
        return HttpResponse("socio no existente.")


def deporteFormulario(req):
    if req.method == 'POST':
        miFormulario = DeporteFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            deporte = Deporte(
                nombre=data["nombre"], fecha_inicio=data["fecha_inicio"], fecha_fin=data["fecha_fin"])
            deporte.save()
            return render(req, "inicio.html")
    else:
        miFormulario = DeporteFormulario()
        return render(req, "deporteFormulario.html", {"miFormulario": miFormulario})


def busquedaDeporte(req):
    return render(req, "busquedaDeporte.html")


def buscar2(req: HttpRequest):

    if req.GET['nombre']:
        nombre = req.GET['nombre']
        deportes = Deporte.objects.filter(nombre=nombre)
        return render(req, "resultadoBusqueda2.html", {"deportes": deportes})
    else:
        return HttpResponse("Deporte no existente.")


def eventoFormulario(req):
    if req.method == 'POST':
        miFormulario = EventoFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            evento = Evento(titulo=data["titulo"], fecha=data["fecha"]
                            )

            evento.save()

            return render(req, "inicio.html")

    else:
        miFormulario = EventoFormulario()
        return render(req, "eventoFormulario.html", {"miFormulario": miFormulario})


def busquedaEvento(req):
    return render(req, "busquedaEvento.html")


def buscar3(req: HttpRequest):

    if req.GET['titulo']:
        titulo = req.GET['titulo']
        evento = Evento.objects.get(titulo=titulo)
        return render(req, "resultadoBusqueda3.html", {"evento": evento})
    else:
        return HttpResponse("Evento no existente.")
