from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "avatar",
            "address",
            "phone_number",
        )
