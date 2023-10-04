from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm


def inicio_usuario(req):
    return render(req, "inicio_usuario.html")


def login_view(req):
    if req.user.is_authenticated:
        return redirect("inicio_usuario.html")
    if req.method == "POST":
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect("inicio_usuario")
    else:
        form = AuthenticationForm()
    return render(req, "login.html", {"form": form})


def logout_view(req):
    logout(req)
    return redirect("inicio_usuario")


def signup_view(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect("inicio_usuario")
    else:
        form = UserCreationForm()
    return render(req, "signup.html", {"form": form})


@login_required
def view_profile(req):
    user = req.user
    return render(req, "profile.html", {"user": user})


@login_required
def edit_profile(req):
    if req.method == "POST":
        form = CustomUserChangeForm(req.POST, instance=req.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserChangeForm(instance=req.user)

    return render(req, "edit_profile.html", {"form": form})
