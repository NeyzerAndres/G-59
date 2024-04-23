from django.db import models

# Create your models here.

class CAMPOS(models.Model):
    cedula = models.IntegerField('Cedula')
    analista = models.CharField('Nombre analista',max_length=50)
    
    
