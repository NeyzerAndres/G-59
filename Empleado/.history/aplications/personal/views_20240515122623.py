from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class EmpleadosListView(ListView):
    template_name = 'templates\personal\mostrar.html'




