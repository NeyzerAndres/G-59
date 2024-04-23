from django.urls import path
from . import views

urlpatterns=[
    path('listar-todo/', views.EmpleadosListView.as_view()),
    path('listar-area/', views.HabibilidadListView.as_view()),
    path('usuarios/', views.UsuarioListView.as_view()),
    path('filtro/', views.ListEmpleadoClave.as_view()),
    #path('habilidades/', views.ListarHabilidadEmpleado.as_view()),
            ]
