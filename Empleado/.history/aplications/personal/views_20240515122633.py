from django.shortcuts import render
from django.views.generic import ListView
from 
# Create your views here.

class EmpleadosListView(ListView):
    template_name = 'personal\mostrar.html'
    model




