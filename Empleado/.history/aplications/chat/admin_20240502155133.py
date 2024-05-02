from django.contrib import admin
from . import models

class RoomAdmin(admin.ModelAdmin):
    list_display = ('tipo_pqrs','proveedor','servicio','estado')
    list_filter = ('tipo_pqrs','proveedor')
    search_fields = ['id',]    

admin.site.register(models.Room)
# Register your models here.
