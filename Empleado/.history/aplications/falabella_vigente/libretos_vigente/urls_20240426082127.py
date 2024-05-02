from django.urls import path
from . import views
app = "libretos_vigente_app"

urlpatterns = [
    path("libreto31/",views.Libreto31TemplateView.as_view()),   
]