from django.contrib import admin
from .models import Socio, Evento, Deporte
# Register your models here.


class SocioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'correo', 'edad']


class DeporteAdmin(admin.ModelAdmin):
    list_filter = ['nombre']


admin.site.register(Socio, SocioAdmin)
admin.site.register(Evento)
admin.site.register(Deporte, DeporteAdmin)
