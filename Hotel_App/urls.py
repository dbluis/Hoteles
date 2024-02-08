from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crearUser/", views.crearUser, name="crearUser"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout")
]
