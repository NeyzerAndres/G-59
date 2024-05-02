from django.contrib import admin
from . import models

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id','name','user')
    list_filter = ('name','user')
    search_fields = ['id',]    

admin.site.register(models.Room,)
# Register your models here.
