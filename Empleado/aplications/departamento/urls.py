from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path('serpiente/',views.SerpienteView.as_view(), name= 'juego'),
    path('Agregar_departamento/',views.NuevoRegistro.as_view(), name= 'agregar'),
]