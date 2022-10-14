from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    antiguedad = models.IntegerField()
    fecha_fabricacion = models.DateField()
    
    # def __str__(self):
    #     return f'{self.modelo} {self.marca}'