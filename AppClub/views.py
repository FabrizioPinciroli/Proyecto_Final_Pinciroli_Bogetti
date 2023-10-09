from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Deporte, Evento
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def inicio(req):
    return render(req, "inicio.html")


class DeporteList(ListView):
    model = Deporte
    template_name = "deporte_list.html"
    context_object_name = "deportes"


class DeporteDetail(DetailView):
    model = Deporte
    template_name = "deporte_detail.html"
    context_object_name = "deporte"


class DeporteCreate(LoginRequiredMixin, CreateView):
    model = Deporte
    template_name = "deporte_create.html"
    fields = "__all__"
    success_url = reverse_lazy("listarDeportes")


class DeporteUpdate(LoginRequiredMixin, UpdateView):
    model = Deporte
    template_name = "deporte_update.html"
    fields = "__all__"
    success_url = reverse_lazy("listarDeportes")


class DeporteDelete(LoginRequiredMixin, DeleteView):
    model = Deporte
    template_name = "deporte_delete.html"
    success_url = reverse_lazy("listarDeportes")


class EventoList(ListView):
    model = Evento
    template_name = "evento_list.html"
    context_object_name = "eventos"


class EventoDetail(DetailView):
    model = Evento
    template_name = "evento_detail.html"
    context_object_name = "evento"


class EventoCreate(LoginRequiredMixin, CreateView):
    model = Evento
    template_name = "evento_Create.html"
    fields = "__all__"
    success_url = reverse_lazy("listarEventos")


class EventoUpdate(LoginRequiredMixin, UpdateView):
    model = Evento
    template_name = "evento_update.html"
    fields = "__all__"
    success_url = reverse_lazy("listarEventos")


class EventoDelete(LoginRequiredMixin, DeleteView):
    model = Evento
    template_name = "evento_delete.html"
    success_url = reverse_lazy("listarEventos")
