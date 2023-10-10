from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import SignupForm, EditProfileForm
from .models import Perfil
from AppClub.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio_usuario(request, mensaje=None):
    if mensaje:
        return render(request, "inicio.html", {"mensaje": mensaje})
    else:
        return render(request, "inicio.html")


def login_view(req):
    if req.method == "POST":
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(req, username=username, password=password)
            if user:
                login(req, user)
                return render(
                    req, "inicio.html", {"mensaje": f"Bienvenido {username}!"}
                )
    else:
        form = AuthenticationForm()
    return render(req, "login.html", {"form": form})


@login_required
def logout_view(req):
    logout(req)
    return redirect("Inicio")


def signup_view(req):
    if req.method == "POST":
        form = SignupForm(req.POST, req.FILES)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.set_password(form.cleaned_data["password1"])
            perfil.save()
            login(req, perfil)
            return redirect("profile")
    else:
        form = SignupForm()
    return render(req, "signup.html", {"form": form})


@login_required
def profile_view(req):
    perfil = Perfil.objects.get(username=req.user.username)
    return render(req, "profile.html", {"perfil": perfil})


@login_required
def edit_profile(req):
    if req.method == "POST":
        form = EditProfileForm(req.POST, req.FILES, instance=req.user)
        if form.is_valid():
            form.save()
            return render(
                req,
                "inicio.html",
                {"mensaje": f"Los datos fueron actualizados con éxito."},
            )
    else:
        form = EditProfileForm(instance=req.user)

    return render(req, "edit_profile.html", {"form": form})


@login_required
def change_password(req):
    if req.method == "POST":
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(req, user)
            return render(
                req,
                "inicio.html",
                {"mensaje": f"La contraseña fue cambiada con éxito."},
            )
    else:
        form = PasswordChangeForm(req.user)

    return render(req, "change_password.html", {"form": form})
