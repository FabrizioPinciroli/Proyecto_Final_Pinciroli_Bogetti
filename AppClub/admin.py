from django.contrib import admin
from .models import Noticia, Evento, Deporte, Contacto


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ["titulo", "subtitulo", "fecha", "tema", "imagen"]
    list_filter = ["tema"]


class DeporteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "categoria"]
    list_filter = ["categoria"]


class EventoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "fecha", "descripcion", "deporte"]
    list_filter = ["deporte"]


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Deporte, DeporteAdmin)
admin.site.register(Contacto)
