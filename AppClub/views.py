from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Socio, Deporte, Evento
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


class SocioList(ListView):
    model = Socio
    template_name = "socio_list.html"
    context_object_name = "socios"


class SocioDetail(DetailView):
    model = Socio
    template_name = "socio_detail.html"
    context_object_name = "socio"


class SocioCreate(CreateView):
    model = Socio
    template_name = "socio_create.html"
    fields = ['nombre', 'apellido', 'edad', 'correo']
    success_url = '/AppClub/'


class SocioUpdate(UpdateView):
    model = Socio
    template_name = "socio_update.html"
    fields = ('__all__')
    success_url = '/AppClub/listaSocios'


class SocioDelete(DeleteView):
    model = Socio
    template_name = "socio_delete.html"
    success_url = '/AppClub/'


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
                nombre=data["nombre"], descripcion=data["descripcion"], fecha_inicio=data["fecha_inicio"], fecha_fin=data["fecha_fin"])
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
        deportes = Deporte.objects.filter(nombre__icontains=nombre)
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


def listaSocios(req):

    socios = Socio.objects.all()

    return render(req, "listaSocios.html", {"socios": socios})


def listaDeportes(req):

    deportes = Deporte.objects.all()

    return render(req, "listaDeportes.html", {"deportes": deportes})


def listaEventos(req):

    eventos = Evento.objects.all()

    return render(req, "listaEventos.html", {"eventos": eventos})


def eliminarSocio(req, id):
    if req.method == 'POST':

        socio = Socio.objects.get(id=id)
        socio.delete()

        socios = Socio.objects.all()

        return render(req, "listaSocios.html", {"socios": socios})


def eliminarDeporte(req, id):
    if req.method == 'POST':

        deporte = Deporte.objects.get(id=id)
        deporte.delete()

        deportes = Deporte.objects.all()

        return render(req, "listaDeportes.html", {"deportes": deportes})


def eliminarEvento(req, id):

    if req.method == 'POST':

        evento = Evento.objects.get(id=id)
        evento.delete()

        eventos = Evento.objects.all()

        return render(req, "listaEventos.html", {"eventos": eventos})


def editar_socio(req, id):

    socio = Socio.objects.get(id=id)

    if req.method == 'POST':
        miFormulario = SocioFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            socio.nombre = data["nombre"]
            socio.apellido = data["apellido"]
            socio.edad = data["edad"]
            socio.correo = data["correo"]

            socio.save()

            return render(req, "inicio.html")
    else:
        miFormulario = SocioFormulario(initial={
            "nombre": socio.nombre,
            "apellido": socio.apellido,
            "edad": socio.edad,
            "correo": socio.correo,
        })

        return render(req, "editarSocio.html", {"miFormulario": miFormulario, "id": socio.id})


def editar_deporte(req, id):

    deporte = Deporte.objects.get(id=id)

    if req.method == 'POST':
        miFormulario = DeporteFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            deporte.nombre = data["nombre"]
            deporte.descripcion = data["descripcion"]
            deporte.fecha_inicio = data["fecha_inicio"]
            deporte.fecha_fin = data["fecha_fin"]
            deporte.save()

            return render(req, "inicio.html")
    else:
        miFormulario = DeporteFormulario(initial={
            "nombre": deporte.nombre,
            "descripcion": deporte.descripcion,
            "fecha_inicio": deporte.fecha_inicio,
            "fecha_fin": deporte.fecha_fin,
        })

        return render(req, "editarDeporte.html", {"miFormulario": miFormulario, "id": deporte.id})


def editar_evento(req, id):

    evento = Evento.objects.get(id=id)

    if req.method == 'POST':
        miFormulario = EventoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            evento.titulo = data["titulo"]
            evento.fecha = data["fecha"]

            evento.save()

    else:
        miFormulario = EventoFormulario(initial={
            "titulo": evento.titulo,
            "fecha": evento.fecha,
        })

        return render(req, "editarEvento.html", {"miFormulario": miFormulario, "id": evento.id})
