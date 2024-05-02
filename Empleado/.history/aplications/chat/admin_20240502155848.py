from django.contrib import admin
from . import models

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id','name','user')
    search_fields = ['id',]    

admin.site.register(models.Room,RoomAdmin)
# Register your models here.
