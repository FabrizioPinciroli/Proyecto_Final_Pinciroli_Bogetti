from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio_usuario, name="inicio_usuario"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("signup/", signup_view, name="signup"),
    path("profile/", profile_view, name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
]
