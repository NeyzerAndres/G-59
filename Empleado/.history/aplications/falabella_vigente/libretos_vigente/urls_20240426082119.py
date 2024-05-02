from django.urls import path
from . import views
app = "libretos_vigente_app"

urlpatterns = [
    path("libreto31/",views.),   
]