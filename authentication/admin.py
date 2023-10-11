from django.contrib import admin
from .models import Perfil

# Register your models here.


class PerfilAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "domicilio",
        "telefono",
        "deporte",
        "evento",
        "avatar",
    ]
    list_filter = [
        "is_active",
        "is_staff",
        "deporte",
        "evento",
    ]


admin.site.register(Perfil, PerfilAdmin)
