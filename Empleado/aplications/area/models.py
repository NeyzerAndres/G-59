from django.db import models
from django.contrib.auth.models import Group
# Create your models here.


class Area(models.Model):
    area = models.CharField('Area', max_length = 30, unique = True)
    grupos = models.ManyToManyField(Group)
    
    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        ordering = ['-id']
    
    def __str__(self):
        return f'{self.id}-{self.area}'
    