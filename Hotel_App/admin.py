from django.contrib import admin
from .models import Hoteles, Habitaciones, Ciudad
# Register your models here.


class HotelAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]

admin.site.register(Ciudad)
admin.site.register(Hoteles)
admin.site.register(Habitaciones)
