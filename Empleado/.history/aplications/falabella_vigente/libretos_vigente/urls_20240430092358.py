from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView
from .views import ChangePasswordView

urlpatterns = [

]


app_name = "libretos_vigente_app"

urlpatterns = [
    path("libreto31/",views.Libreto31TemplateView.as_view(),name='libreto31'),   
]