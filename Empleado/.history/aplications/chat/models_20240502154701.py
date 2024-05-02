from django.db import models

# Create your models here.

class Room (models.Model):
    name = models.CharField(max_length= 100, unique=True, verbose_name='Nombre')
    users = models.ManyToManyField(User, related_name='rooms_joined', blank=True) 