from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil


class SignupForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "fecha_nacimiento",
            "telefono",
            "domicilio",
            "avatar",
        ]


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            "first_name",
            "last_name",
            "email",
            "fecha_nacimiento",
            "telefono",
            "domicilio",
            "avatar",
        ]
