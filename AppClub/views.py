from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Socio, Deporte, Evento
from .forms import *
from django.urls import reverse_lazy
# Create your views here.


def inicio(req):
    return render(req, "inicio.html")


class SocioList(ListView):
    model = Socio
    template_name = 'socio_list.html'
    context_object_name = 'socios'


class SocioDetail(DetailView):
    model = Socio
    template_name = 'socio_detail.html'
    context_object_name = 'socio'


class SocioCreate(CreateView):
    model = Socio
    template_name = 'socio_create.html'
    fields = '__all__'
    success_url = reverse_lazy('listarSocios')


class SocioUpdate(UpdateView):
    model = Socio
    template_name = 'socio_update.html'
    fields = '__all__'
    success_url = reverse_lazy('listarSocios')


class SocioDelete(DeleteView):
    model = Socio
    template_name = 'socio_delete.html'
    success_url = reverse_lazy('listarSocios')


class DeporteList(ListView):
    model = Deporte
    template_name = 'deporte_list.html'
    context_object_name = 'deportes'


class DeporteDetail(DetailView):
    model = Deporte
    template_name = 'deporte_detail.html'
    context_object_name = 'deporte'


class DeporteCreate(CreateView):
    model = Deporte
    template_name = 'deporte_create.html'
    fields = '__all__'
    success_url = reverse_lazy('listarDeportes')


class DeporteUpdate(UpdateView):
    model = Deporte
    template_name = 'deporte_update.html'
    fields = '__all__'
    success_url = reverse_lazy('listarDeportes')


class DeporteDelete(DeleteView):
    model = Deporte
    template_name = 'deporte_delete.html'
    success_url = reverse_lazy('listarDeportes')


class EventoList(ListView):
    model = Evento
    template_name = 'evento_list.html'
    context_object_name = 'eventos'


class EventoDetail(DetailView):
    model = Evento
    template_name = 'evento_detail.html'
    context_object_name = 'evento'


class EventoCreate(CreateView):
    model = Evento
    template_name = 'evento_Create.html'
    fields = '__all__'
    success_url = reverse_lazy('listarEventos')


class EventoUpdate(UpdateView):
    model = Evento
    template_name = 'evento_update.html'
    fields = '__all__'
    success_url = reverse_lazy('listarEventos')


class EventoDelete(DeleteView):
    model = Evento
    template_name = 'evento_delete.html'
    success_url = reverse_lazy('listarEventos')
