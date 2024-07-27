from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    ckeditor = RichTextField()
    def __str__(self):
        return f'{self.id}-{self.titulo}'
        