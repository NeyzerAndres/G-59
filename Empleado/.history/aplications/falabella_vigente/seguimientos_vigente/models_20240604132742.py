from django.db import models

# Create your models here.
class Prueba(models.Model):
    ESTADO = (
        ("Activo","Activo"),
        ("Inactivo","Inactivo"),
            )
    nombre = models.CharField('Nombre', max_length=100)
    estado = models.CharField('Estado', max_length=20)
    
    class Meta:
        dbname = 'prueba'
        verbose_name = 'Tabla_Prueba'
        verbose_name_plural = 'Tabla_Pruebas'
        
    def __str__(self):
        return self.nombre
        
class Relacion(models.Model):
    ESTADO = (
        ("Activo","Activo"),
        ("Inactivo","Inactivo"),
            )
    nombre = models.CharField('Nombre', max_length=100)
    nombre = models.ForeignKey('Nombre', max_length=100)
    estado = models.CharField('Estado', max_length=20)
    
    class Meta:
        dbname = 'relacion'
        verbose_name = 'Tabla_Relacion'
        verbose_name_plural = 'Tabla_Relaciones'
        
    def __str__(self):
        return self.nombre