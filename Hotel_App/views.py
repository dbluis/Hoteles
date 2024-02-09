from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Habitaciones, Hoteles


def index(request):
    hotel = Hoteles.objects.all()
    return render(request, "index.html", {
        "hoteles": hotel
    })

# Usuario


def crearUser(request):
    if request.method == "GET":
        return render(request, "User/crearUser.html")
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect(index)
            except IntegrityError:
                return render(request, "User/crearUser.html", {"error": "El usuario ya existe"})


def signout(request):
    logout(request)
    return redirect(index)


def signin(request):
    if request.method == "GET":
        return render(request, "User/signin.html")
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "User/signin.html", {"error": "El usuario o contraseña no coinciden"})
        else:
            login(request, user)
            return redirect(index)

# Habitaciones


def habitaciones_de_hotel(request, hotel_id):
    hotel = Hoteles.objects.get(pk=hotel_id)
    habitaciones = hotel.habitaciones_set.all()
    # contador
    habitaciones_libres = hotel.habitaciones_set.filter(habilitado=True)
    habitaciones_libres_count = habitaciones_libres.count()
    return render(request, 'habitaciones.html', {'hotel': hotel, 'habitaciones': habitaciones, 'habitaciones_libres_count': habitaciones_libres_count})

# Cambiar estado de habilitado


def cambiar_estado_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitaciones, pk=habitacion_id)
    # Verifica si el formulario se envió con el método POST
    if request.method == 'POST':
        # Cambia el estado habilitado de la habitación
        habitacion.habilitado = not habitacion.habilitado
        habitacion.save()
    # Redirige de vuelta a la página anterior
    return redirect('index')
