from typing import Any
from django.db import models
from ckeditor.fields import RichTextField
from aplications.departamento.models import Departamento

# Create your models here.
class Habilidad_empleados(models.Model):
    habilidad = models.CharField(("Habilidad"), max_length=50, unique= True)
    
    class Meta:
        verbose_name = 'Habilidad de Empleado'
        verbose_name_plural = 'Habilidades de los Empleados'

    def __str__(self):
        return f'{self.habilidad}'    

    
class Empleado(models.Model):   
    """Modelo de la tambla empleado"""
    Job_Choices = ( 
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro')
        )
#     #Contador
#     #administrador
#     #Economista
#     #Otro
    first_name = models.CharField(("Nombres"), max_length=50)
    last_name = models.CharField(("Apellidos"), max_length=50,unique=True)
    job = models.CharField(("Trabajo"), max_length=50, choices = Job_Choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) 
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidad_empleados)
    hoja_vida= RichTextField()
  
    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleado en Departamentos'
        unique_together = 'job','first_name'    
        ordering = ['departamento']
    
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
    
