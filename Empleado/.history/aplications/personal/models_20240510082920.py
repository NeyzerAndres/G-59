from django.db import models

# Create your models here.
class Empleados(models.Model):
    identificaion = models.BigIntegerField('Identificacion')
    