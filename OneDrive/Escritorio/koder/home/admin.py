from django.contrib import admin
from home.models import Cliente, Vehiculo

# Register your models here.

admin.site.register(Vehiculo)

admin.site.register(Cliente)