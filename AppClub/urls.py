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
    path('listaSocios/', listaSocios, name="listaSocios"),
    path('eliminarSocios/<int:id>', eliminarSocio, name="eliminarSocios"),
    path('editarSocios/<int:id>', editar_socio, name="editarSocios"),

    # vistas basadas en clases, editar.
    path('listarSocios/', SocioList.as_view, name="listarSocios"),
    path('detalleSocios/<pk>', SocioDetail.as_view, name="detallarSocios"),
    path('crearSocios/', SocioCreate.as_view, name="crearSocios"),
    path('actualizarSocios/<pk>', SocioUpdate.as_view, name="actualizarSocios"),
    path('deletearSocios/<pk>', SocioDelete.as_view, name="deletearSocios"),




    path('deporte-Formulario/', deporteFormulario, name="deporteFormulario"),
    path('busqueda-deporte/', busquedaDeporte, name="busquedaDeporte"),
    path('buscar2/', buscar2, name="buscar2"),
    path('listaDeportes/', listaDeportes, name="listaDeportes"),
    path('eliminarDeportes/<int:id>', eliminarDeporte, name="eliminarDeportes"),
    path('editarDeportes/<int:id>', editar_deporte, name="editarDeportes"),

    path('evento-Formulario/', eventoFormulario, name="eventoFormulario"),
    path('busqueda-evento/', busquedaEvento, name="busquedaEvento"),
    path('buscar3/', buscar3, name="buscar3"),
    path('listaEventos/', listaEventos, name="listaEventos"),
    path('eliminarEventos/<int:id>', eliminarEvento, name="eliminarEventos"),
    path('editarEventos/<int:id>', editar_evento, name="editarEventos"),



]
