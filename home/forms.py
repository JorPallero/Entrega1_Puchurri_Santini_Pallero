from django import forms
from ckeditor.fields import RichTextFormField

class VehiculoFormulario(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=15)
    color = forms.CharField(max_length=15)
    antiguedad = forms.IntegerField()
    fecha_fabricacion = forms.DateField(required=False)
    
class BusquedaVehiculoFormulario(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    
class Cliente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    domicilio = forms.CharField(max_length=40)
    descripcion = RichTextFormField(required=False)
    
class BusquedaCliente(forms.Form):
    apellido = forms.CharField(max_length=20, required=False)