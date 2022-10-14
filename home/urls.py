from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name='index'),
    path('ver-vehiculos/',views.ver_vehiculos, name='ver vehiculos'),
    path('ver-clientes/',views.ver_clientes, name='ver clientes'),
    path('about/',views.about, name='about'),
]
