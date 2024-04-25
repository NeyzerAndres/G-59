from . import views
from django.urls import path
from .views import Home

app_name = 'home_app'

urlpatterns=[
     path('agregar/', views.AgregarPrueba.as_view(),name='nuevo'),
     #path('succes/', views.SuccesView.as_view(), name= 'felicidades'),
     path('editar/<pk>/', views.ActualizarView.as_view(), name= 'editar_empleado'),
     path('eliminar/<pk>/', views.EmilinarView.as_view(), name= 'eliminar_empleado'),
    # path('home/', views.IndexView.as_view()),
     path('lista/', views.Modelo_PruebaListView.as_view()),
     path('login/', views.LoginTemplateView.as_view()),
     path('base/', views.BaseTemplateView.as_view()),
     path('header/', views.HeaderTemplateView.as_view()),
     path('/', views.GeneralTemplateView.as_view()),
    # path('Pruebas/', views.Modelo_PruebaListView.as_view()),
     path('',Home.as_view(),name='home'),
            ]
    
    