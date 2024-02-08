from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")

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

# Hoteles
