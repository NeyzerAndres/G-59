from django.db import models

class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    # Agrega otros campos según tu modelo

