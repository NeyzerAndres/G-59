from django.contrib import admin
from . import models

class RoomAdmin(admin.ModelAdmin):
    fields = ''
    

admin.site.register(models.Room)
# Register your models here.
