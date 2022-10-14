from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from home.forms import VehiculoFormulario
from datetime import datetime
from home.models import Vehiculo

# Create your views here.

def index(request):
    return render (request, 'home/index.html')

def ver_clientes(request):
    return render (request, 'home/ver_clientes.html') 

def about(request):
    return render (request, 'home/about.html')

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
    
    vehiculos = Vehiculo.objects.all()
 
    return render(request, 'home/ver_vehiculos.html',{'vehiculos':vehiculos})
