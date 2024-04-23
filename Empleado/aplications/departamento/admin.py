from django.contrib import admin
from .models import Departamento
# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_filter = ['shor_name']

admin.site.register(Departamento,DepartamentoAdmin)
