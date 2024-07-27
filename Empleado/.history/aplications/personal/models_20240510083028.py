from django.db import models

# Create your models here.
class Empleados(models.Model):
    identificaion = models.BigIntegerField('Identificacion')
    nombres = models.CharField('Nombres', max_length=30)
    apellidos = models.CharField('Apellidos', max_length=30)
    edad = models.BigIntegerField('Edad')