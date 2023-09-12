from django import forms


class SocioFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    correo = forms.CharField(max_length=60)


class DeporteFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=60)
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()


class EventoFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    fecha = forms.DateField()
