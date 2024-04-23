from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# Create your views here.

class pruebatemplate(TemplateView):
    template_name = 'empleados/index.html'