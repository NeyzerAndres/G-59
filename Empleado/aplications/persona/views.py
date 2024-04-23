from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView
from . import models
from django.contrib.auth.models import User
# Create your views here.

class EmpleadosListView(ListView):
    template_name = 'persona/listar_todo.html'
    paginate_by = 2
    model = User
    context_object_name = 'lista'
    
class HabibilidadListView(ListView):
    template_name = 'persona/listar_area.html'
    
    def get_queryset(self):
        #area = self.kwargs['shorname']
        lista = models.Empleado.objects.filter(first_name= 'area',)
        return lista
    
    context_object_name = 'Area'
    
class UsuarioListView(TemplateView):
    template_name = 'includes/base.html'
    context_object_name = 'usuarios'
    
class ListEmpleadoClave(TemplateView):
    template_name = 'persona/filtro.html'
    
# class ListarHabilidadEmpleado(ListView):
#     template_name = 'persona/habilidad.html'
#     context_object_name = 'habilidades'
#     def get_queryset(self):
#         queryset = models.Empleado.objects.get(id = 2)
#         return queryset

class AgregarUsuario(CreateView):
    template_name = 'persona'






