from . import views
from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView
from .views import ChangePasswordView
app_name = 'home_app'

urlpatterns=[
     path('lista/', views.Modelo_PruebaListView.as_view(),name='lista'),
     path('login/', views.LoginTemplateView.as_view(), name='login'),
     path('base/', views.BaseTemplateView.as_view(), name='base'),
     path('header/', views.HeaderTemplateView.as_view(), name='header'),
     path('', views.GeneralTemplateView.as_view(),name='general'),
     path('galeria', views.GaleriaTemplateView.as_view(),name='galeria'),
     path('change-password/', ChangePasswordView.as_view(), name='change_password'),
     path('change-password/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
          ]
