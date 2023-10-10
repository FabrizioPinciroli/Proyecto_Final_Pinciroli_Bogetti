from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Noticia, Deporte, Evento
from .forms import NoticiaFormulario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def inicio(req):
    return render(req, "inicio.html")


def about_us(req):
    return render(req, "about_us.html")


class NoticiaList(ListView):
    model = Noticia
    template_name = "noticia_list.html"
    context_object_name = "noticias"


class NoticiaDetail(DetailView):
    model = Noticia
    template_name = "noticia_detail.html"
    context_object_name = "noticia"


class NoticiaCreate(LoginRequiredMixin, CreateView):
    model = Noticia
    template_name = "noticia_create.html"
    form_class = NoticiaFormulario
    success_url = reverse_lazy("Inicio")

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context


class NoticiaUpdate(LoginRequiredMixin, UpdateView):
    model = Noticia
    template_name = "noticia_update.html"
    form_class = NoticiaFormulario
    success_url = reverse_lazy("listarNoticias")


class NoticiaDelete(DeleteView):
    model = Noticia
    template_name = "noticia_delete.html"
    success_url = reverse_lazy("listarNoticias")


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
