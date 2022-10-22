from django.urls import path
from home import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('ver-vehiculos/',views.ver_vehiculos, name='ver_vehiculos'),
    path('about/',views.about, name='about'),
    path('crear-vehiculo/',views.crear_vehiculo, name='crear_vehiculo'),
    path('contact/',views.contact, name='contact'),
    path('clientes/',views.ListarClientes.as_view(), name='listar_clientes'),
    path('clientes/crear/',views.CrearCliente.as_view(), name='crear_cliente'),
    path('clientes/<int:pk>/editar/',views.EditarCliente.as_view(), name='editar_cliente'),
    path('clientes/<int:pk>/eliminar/',views.EliminarCliente.as_view(), name='eliminar_cliente'),
]
