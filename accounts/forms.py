from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MiFormularioDeCreacion(UserCreationForm):
    
    username = forms.CharField(label = 'Usuario', max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        

class EditarFormulario (forms.Form):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    avatar = forms.ImageField(required=False)
    descripcion = forms.CharField(label='Cómo me describo?', required=False)
    link_pagina = forms.CharField(label='Agregá un link si tenés blog', required=False)