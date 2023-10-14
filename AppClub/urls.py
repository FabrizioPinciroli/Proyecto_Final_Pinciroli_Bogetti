from django.urls import path
from AppClub.views import *
from authentication.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("about_us/", about_us, name="about_us"),
    path("contacto/", contacto, name="contacto"),
    path("listarNoticias/", NoticiaList.as_view(), name="listarNoticias"),
    path("detallarNoticias/<pk>/", NoticiaDetail.as_view(), name="detallarNoticias"),
    path("crearNoticias/", NoticiaCreate.as_view(), name="crearNoticias"),
    path(
        "actualizarNoticias/<pk>/", NoticiaUpdate.as_view(), name="actualizarNoticias"
    ),
    path("eliminarNoticias/<pk>/", NoticiaDelete.as_view(), name="eliminarNoticias"),
    path("listarDeportes/", DeporteList.as_view(), name="listarDeportes"),
    path("detalleDeportes/<pk>/", DeporteDetail.as_view(), name="detallarDeportes"),
    path("crearDeportes/", DeporteCreate.as_view(), name="crearDeportes"),
    path(
        "actualizarDeportes/<pk>/", DeporteUpdate.as_view(), name="actualizarDeportes"
    ),
    path("eliminarDeportes/<pk>/", DeporteDelete.as_view(), name="eliminarDeportes"),
    path("listarEventos/", EventoList.as_view(), name="listarEventos"),
    path("detalleEventos/<pk>/", EventoDetail.as_view(), name="detallarEventos"),
    path("crearEventos/", EventoCreate.as_view(), name="crearEventos"),
    path("actualizarEventos/<pk>/", EventoUpdate.as_view(), name="actualizarEvento"),
    path("eliminarEventos/<pk>/", EventoDelete.as_view(), name="eliminarEventos"),
    path(
        "noticia/<int:noticia_id>/comentar/",
        CrearComentario.as_view(),
        name="CrearComentario",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
