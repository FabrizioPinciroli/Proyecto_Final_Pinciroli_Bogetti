from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_usuario, name="inicio_usuario"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("profile/", views.view_profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
]
