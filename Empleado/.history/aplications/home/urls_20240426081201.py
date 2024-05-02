from . import views
from django.urls import path

app_name = 'home_app'

urlpatterns=[
     path('lista/', views.Modelo_PruebaListView.as_view(),name='lista'),
     path('login/', views.LoginTemplateView.as_view(), name='login'),
     path('base/', views.BaseTemplateView.as_view(), name='base'),
     path('header/', views.HeaderTemplateView.as_view(), name='header'),
     path('', views.GeneralTemplateView.as_view(),name='general'),
     path('galeria', views.GaleriaTemplateView.as_view(),name='galeria'),
            ]
    
    