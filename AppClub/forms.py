from django import forms
from .models import Noticia, Contacto, Comentario


class NoticiaFormulario(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NoticiaFormulario, self).__init__(*args, **kwargs)
        self.fields["imagen"].widget.attrs["accept"] = "image/*"


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

    mensajes = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"placeholder": "Escribe tu mensaje..."}),
    )


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["comentario"]

    comentario = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"placeholder": "Comentario"}),
    )
