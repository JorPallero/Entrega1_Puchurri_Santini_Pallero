from django.shortcuts import render, redirect
from home.forms import BusquedaVehiculoFormulario, VehiculoFormulario
from datetime import datetime
from home.models import Vehiculo, Cliente
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render (request, 'home/inicio.html')

def about(request):
    return render (request, 'home/about.html')

def contact(request):
    return render (request, 'home/contact.html')

@login_required
def crear_vehiculo(request):
    
    if request.method == 'POST':
        
        formulario = VehiculoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            modelo = data['modelo']
            marca = data['marca']
            color = data['color']
            antiguedad = data['antiguedad']
            
            fecha_fabricacion = data['fecha_fabricacion']
            if not fecha_fabricacion:
                fecha_fabricacion = datetime.now()
            
            vehiculo = Vehiculo(modelo=modelo, marca=marca, color=color, antiguedad=antiguedad, fecha_fabricacion=fecha_fabricacion)
            vehiculo.save()
            
        return redirect('ver_vehiculos')
    
    formulario = VehiculoFormulario()
    
    return render(request, 'home/crear_vehiculo.html',{'formulario':formulario})

def ver_vehiculos(request):
    
    marca = request.GET.get('marca', None)
    
    if marca:
        vehiculos = Vehiculo.objects.filter(marca__icontains=marca)
    else:
        vehiculos = Vehiculo.objects.all()
    
    formulario = BusquedaVehiculoFormulario()
 
    return render(request, 'home/ver_vehiculos.html',{'vehiculos':vehiculos, 'formulario':formulario})

def ver_clientes(request):
    return render (request, 'home/ver_clientes.html') 

def registrar(request):
    formulario = ''
    return render(request, 'accounts/registrar.html', {'formulario': formulario})

class ListarClientes(ListView):
    model = Cliente
    template_name = 'home/listar_clientes.html'


class CrearCliente(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'home/crear_cliente.html'
    success_url = '/clientes'
    fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento', 'domicilio', 'descripcion']
    
    
class EditarCliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'home/editar_cliente.html'
    success_url = '/clientes'
    fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento', 'domicilio']
    
    
class EliminarCliente(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'home/eliminar_cliente.html'
    success_url = '/clientes'
    
class VerCliente(DetailView):
    model = Cliente 
    template_name = 'home/ver_cliente.html'
    
    
    

