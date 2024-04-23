from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import (FormView)
from django.views.generic import TemplateView
from . import forms
# Create your views here.

class NuevoRegistro(FormView):
    template_name = 'departamento/nuevo.html'
    form_class = forms.NuevoDepartamento
    success_url = '/'
    
    def form_valid(self, form):
        print('Estamos en el Formulario')
        return super(NuevoRegistro).form_valid(form)

class SerpienteView(TemplateView):
    template_name = "departamento/juego.html"
