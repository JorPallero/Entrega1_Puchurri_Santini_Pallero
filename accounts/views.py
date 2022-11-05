from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from accounts.forms import MiFormularioDeCreacion, EditarFormulario
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import ExtensionUsuario

def mi_login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            extensionusuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
    return render(request, 'accounts/login.html', {'formulario': formulario})
    
def registrar(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = MiFormularioDeCreacion()
    return render(request, 'accounts/registrar.html', {'formulario': formulario})

@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html', {})

@login_required
def editar_perfil(request):
    
    user = request.user
    mas_datos_usuario, _ = ExtensionUsuario.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        formulario=EditarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name') 
            if data.get('last_name'):
                user.last_name = data.get('last_name')
                
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuario.descripcion = data.get('descripcion') if data.get('descripcion') else mas_datos_usuario.descripcion
            mas_datos_usuario.link_pagina = data.get('link_pagina') if data.get('link_pagina') else mas_datos_usuario.link_pagina
            mas_datos_usuario.avatar = data.get('avatar') if data.get('avatar') else mas_datos_usuario.avatar
            
            mas_datos_usuario.save()
            user.save()
            return redirect('perfil')
        else:
            return render(request, 'accounts/editar_perfil.html', {'formulario': formulario})
    else:
        formulario=EditarFormulario(
            initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'avatar': mas_datos_usuario.avatar,
                'descripcion': user.extensionusuario.descripcion,
                'link_pagina': user.extensionusuario.link_pagina
                }
            )
    return render(request, 'accounts/editar_perfil.html', {'formulario':formulario})


class CambiarContraseña(LoginRequiredMixin,PasswordChangeView):
    template_name = 'accounts/cambiar_contraseña.html'
    success_url = '/accounts/perfil/'