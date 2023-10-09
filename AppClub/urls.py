from django.urls import path
from AppClub.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    # vistas basadas en clases, editar.
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
