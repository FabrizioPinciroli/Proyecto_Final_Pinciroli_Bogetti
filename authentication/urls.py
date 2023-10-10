from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", inicio_usuario, name="inicio_usuario"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("signup/", signup_view, name="signup"),
    path("profile/", profile_view, name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("change_password/", change_password, name="change_password"),
]
