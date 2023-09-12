from django.urls import path
from AppClub.views import *
urlpatterns = [

    path('', inicio, name="Inicio"),
    path('socio/', socio, name="Socio"),
    path('deporte/', deporte, name="Deporte"),
    path('evento/', evento, name="Evento"),
    path('lista-socios/', listar_socios, name="listaSocios"),

    path('socio-Formulario/', socioFormulario, name="socioFormulario"),
    path('busqueda-apellido/', busquedaApellido, name="busquedaApellido"),
    path('buscar/', buscar1, name="buscar1"),

    path('deporte-Formulario/', deporteFormulario, name="deporteFormulario"),
    path('busqueda-deporte/', busquedaDeporte, name="busquedaDeporte"),
    path('buscar2/', buscar2, name="buscar2"),

    path('evento-Formulario/', eventoFormulario, name="eventoFormulario"),
    path('busqueda-evento/', busquedaEvento, name="busquedaEvento"),
    path('buscar3/', buscar3, name="buscar3"),



]
