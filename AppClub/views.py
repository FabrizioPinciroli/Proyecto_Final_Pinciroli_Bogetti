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


# def deporteFormulario(req):
#     if req.method == 'POST':
#         miFormulario = DeporteFormulario(req.POST)
#
#         if miFormulario.is_valid():
#             data = miFormulario.cleaned_data
#             deporte = Deporte(
#                 nombre=data["nombre"], fecha_inicio=data["fecha_inicio"], fecha_fin=data["fecha_fin"])
#
#             deporte.save()
#
#             return render(req, "inicio.html")
#
#     else:
#         miFormulario = DeporteFormulario()
#         return render(req, "deporteFormulario.html", {"miFormulario": miFormulario})
#
#
# def eventoFormulario(req):
#     if req.method == 'POST':
#         miFormulario = EventoFormulario(req.POST)
#
#         if miFormulario.is_valid():
#             data = miFormulario.cleaned_data
#             evento = Evento(titulo=data["titulo"], nombre=data["nombre"], fecha=data["fecha"], descripcion=data["descripcion"]
#                             )
#
#             evento.save()
#
#             return render(req, "inicio.html")
#
#     else:
#         miFormulario = DeporteFormulario()
#         return render(req, "deporteFormulario.html", {"miFormulario": miFormulario})

def busquedaApellido(req):
    return render(req, "busquedaApellido.html")


def buscar(req: HttpRequest):

    if req.GET['Apellido']:
        apellido = req.GET['Apellido']
        socio = Socio.objects.get(apellido=apellido)
        return render(req, "resultadoBusqueda.html", {"socio": socio})
    else:
        return HttpResponse("socio no existente.")
