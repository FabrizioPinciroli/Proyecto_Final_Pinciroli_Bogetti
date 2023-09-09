from django.urls import path
from AppClub.views import *
urlpatterns = [

    path('', inicio, name="Inicio"),
    path('socio/', socio, name="Socio"),
    path('deporte/', deporte, name="Deporte"),
    path('evento/', evento, name="Evento"),
    path('lista-socios/', listar_socios),


]
