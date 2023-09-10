from django.urls import path
from AppClub.views import *
urlpatterns = [

    path('', inicio, name="Inicio"),
    path('socio/', socio, name="Socio"),
    path('deporte/', deporte, name="Deporte"),
    path('evento/', evento, name="Evento"),
    path('lista-socios/', listar_socios, name="listaSocios"),
    path('socio-Formulario/', socioFormulario, name="socioFormulario"),
    # path('deporte-Formulario/', deporteFormulario, name="deporteFormulario"),
    # path('evento-Formulario/', eventoFormulario, name="eventoFormulario"),
    path('busqueda-apellido/', busquedaApellido, name="busquedaApellido"),
    path('buscar/', buscar, name="buscar"),



]
