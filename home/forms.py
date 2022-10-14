from django import forms

class VehiculoFormulario(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=15)
    color = forms.CharField(max_length=15)
    antiguedad = forms.IntegerField()
    fecha_fabricacion = forms.DateField(required=False)