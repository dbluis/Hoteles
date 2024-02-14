from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
class Hoteles(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=300, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Habitaciones(models.Model):
    habitacion = models.CharField(max_length=200)
    hoteles = models.ForeignKey(Hoteles, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=False)

    def __str__(self):
        return self.habitacion
