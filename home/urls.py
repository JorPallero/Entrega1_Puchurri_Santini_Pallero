from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name='index'),
    path('ver-vehiculos/',views.ver_vehiculos, name='ver_vehiculos'),
    path('ver-clientes/',views.ver_clientes, name='ver_clientes'),
    path('about/',views.about, name='about'),
    path('crear-vehiculo/',views.crear_vehiculo, name='crear_vehiculo'),
]
