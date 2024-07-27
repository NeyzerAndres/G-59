from django.db import models

# Create your models here.
class Prueba(models.Model):
    ESTADO = (
        ("Activo","Activo"),
        ("Inactivo","Inactivo"),
            )
    nombre = models.CharField('Nombre', max_length=100)
    estado = models.CharField('Estado', choices=ESTADO, max_length=20)
    
    class Meta:
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
    prueba = models.ManyToManyField(Prueba)
    estado = models.CharField('Estado', choices=ESTADO, max_length=20)
    
    class Meta:
        verbose_name = 'Tabla_Relacion'
        verbose_name_plural = 'Tabla_Relacione  s'
        
    def __str__(self):
        return self.nombre