from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre',max_length=30,)
    shor_name = models.CharField('Nombre Corto',max_length=15)
    anulate = models.BooleanField('Anulado',default =False)    
    
    class Meta:
        verbose_name_plural = 'Departamento'
        ordering = ['-name']
        
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name
