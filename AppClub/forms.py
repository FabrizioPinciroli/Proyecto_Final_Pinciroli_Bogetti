from django import forms
from .models import Noticia, Contacto


class NoticiaFormulario(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = "__all__"


class DeporteFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=60)
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()


class EventoFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    fecha = forms.DateField()


class ContactoFormulario(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"
