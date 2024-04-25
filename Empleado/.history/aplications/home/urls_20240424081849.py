from . import views
from django.urls import path
from . import Home

app_name = 'home_app'

urlpatterns=[
     path('lista/', views.Modelo_PruebaListView.as_view()),
     path('login/', views.LoginTemplateView.as_view()),
     path('base/', views.BaseTemplateView.as_view()),
     path('header/', views.HeaderTemplateView.as_view()),
     path('general/', views.GeneralTemplateView.as_view()),
     path('',Home.as_view(),name='home'),
            ]
    
    