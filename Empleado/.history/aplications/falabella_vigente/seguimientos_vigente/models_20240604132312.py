from django.db import models

# Create your models here.
class Prueba(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    estado = 