from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crearUser/", views.crearUser, name="crearUser"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    # habitaciones
    path('hoteles/<int:hotel_id>/habitaciones/',
         views.habitaciones_de_hotel, name='habitaciones_de_hotel'),
    path('habitaciones/<int:habitacion_id>/cambiar_estado/',
         views.cambiar_estado_habitacion, name='cambiar_estado_habitacion'),
]
