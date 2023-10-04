from django.urls import path
from AppClub.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    # vistas basadas en clases, editar.
    path("listarSocios/", SocioList.as_view(), name="listarSocios"),
    path("detalleSocios/<pk>", SocioDetail.as_view(), name="detallarSocios"),
    path("crearSocios/", SocioCreate.as_view(), name="crearSocios"),
    path("actualizarSocios/<pk>", SocioUpdate.as_view(), name="actualizarSocios"),
    path("eliminarSocios/<pk>", SocioDelete.as_view(), name="eliminarSocios"),
    path("listarDeportes/", DeporteList.as_view(), name="listarDeportes"),
    path("detalleDeportes/<pk>", DeporteDetail.as_view(), name="detallarDeportes"),
    path("crearDeportes/", DeporteCreate.as_view(), name="crearDeportes"),
    path("actualizarDeportes/<pk>", DeporteUpdate.as_view(), name="actualizarDeportes"),
    path("eliminarDeportes/<pk>", DeporteDelete.as_view(), name="eliminarDeportes"),
    path("listarEventos/", EventoList.as_view(), name="listarEventos"),
    path("detalleEventos/<pk>", EventoDetail.as_view(), name="detallarEventos"),
    path("crearEventos/", EventoCreate.as_view(), name="crearEventos"),
    path("actualizarEventos/<pk>", EventoUpdate.as_view(), name="actualizarEvento"),
    path("eliminarEventos/<pk>", EventoDelete.as_view(), name="eliminarEventos"),
]
