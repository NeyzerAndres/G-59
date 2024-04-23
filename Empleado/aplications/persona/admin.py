from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Empleado,Habilidad_empleados
# Register your models here.

#Congiguracion del template administrador modelo Empleado
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'departamento',
                    'Nombre_Completo',)
    #Genera historial de los cambios que se realizan
    def Nombre_Completo(self,obj):
        return f'{obj.first_name} {obj.last_name}'



    #Genera una barra de busqueda para buscar un dato en especifico 
    search_fields = ('first_name',)

    #Agrega un filtro en base al job del Empleado
    list_filter = ('job','habilidades',)
    
    #Este filtro solo funciona en relaciones muchos a muchos
    filter_horizontal = ('habilidades',) 

admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Habilidad_empleados)
