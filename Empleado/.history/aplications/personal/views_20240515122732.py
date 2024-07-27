from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.

class EmpleadosListView(ListView):
    template_name = 'personal\mostrar.html'
    model = models.Empleados
    context_object_name = 'empleados'
        




