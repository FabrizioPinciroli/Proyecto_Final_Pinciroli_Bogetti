from django.contrib import admin
from .models import Evento, Deporte

# Register your models here.


class DeporteAdmin(admin.ModelAdmin):
    list_filter = ["nombre"]


admin.site.register(Evento)
admin.site.register(Deporte, DeporteAdmin)
