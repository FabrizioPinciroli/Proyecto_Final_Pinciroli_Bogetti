from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.inicio_usuario, name="inicio_usuario"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("profile/", views.view_profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
=======
    path("inicio/", inicio, name="inicio"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("view_profile/", view_profile, name="view_profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
>>>>>>> 851ba07728dc7e0b2235d324dba7bfe681fcc466
]
