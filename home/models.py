from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    antiguedad = models.IntegerField()
    fecha_fabricacion = models.DateField()
    
    def __str__(self):
        return f'{self.modelo} {self.marca} {self.color} {self.antiguedad}'
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    domicilio = models.CharField(max_length=40)
    descripcion = RichTextField(null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.edad} {self.fecha_nacimiento} {self.domicilio}'