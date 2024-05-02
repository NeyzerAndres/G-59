from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from .models import Prueba
from django.urls import reverse_lazy
from . import forms

# Create your views here.
class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = [1,2,3,4,5,6,7,9]
    context_object_name = 'Lista_Prueba'    
    
class Modelo_PruebaListView(ListView):
    model = Prueba
    template_name = "home/Pruebas.html"
    context_object_name = 'lista_Prueba01'

class AgregarPrueba(CreateView):
    #Los campos requeridos para hacer funcionar un CrediView
    template_name = "home/agregar.html"
    form_class = forms.PruebaForm
    success_url =reverse_lazy('home_app:nuevo')
    
    
    
class ActualizarView(UpdateView):
    template_name='home/editar.html'
    model = Prueba
    fields = ('__all__')
    success_url = reverse_lazy('home_app:nuevo')
    
    def post(self, request: HttpRequest, *args: str, **kwargs):
        return super().post(request, *args, **kwargs)
class EmilinarView(DeleteView):
    template_name = 'home/eliminar.html'
    model = Prueba 
    success_url = reverse_lazy('home_app:nuevo')
    
class LoginTemplateView(TemplateView):
    template_name = 'includes/login.html'    
    
class BaseTemplateView(TemplateView):
    template_name = 'includes/base.html'    
    
    
class HeaderTemplateView(TemplateView):
    template_name = 'includes/menu.html'    

class GeneralTemplateView(TemplateView):
    template_name = 'includes/general.html'    
    
    
class GaleriaTemplateView(TemplateView):
    template_name = 'home/galeria.html'  
    

    
