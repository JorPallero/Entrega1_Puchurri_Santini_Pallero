from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render (request, 'home/index.html')

def ver_clientes(request):
    return render (request, 'home/ver_clientes.html') 

def ver_vehiculos(request):
    return render (request, 'home/ver_vehiculos.html') 

def about(request):
    return render (request, 'home/about.html')