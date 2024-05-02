from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_change_done')

class Libreto31TemplateView(TemplateView):
    template_name = 'falabella_vigente/libretos/libreto31.html'

    def get_context_data(self, **kwargs):
        context = super(Libreto31TemplateView, self).get_context_data(**kwargs)
        context ['titulo'] = 'Libretos'
        context ['subruta'] = 'Falabella Vigente'
        context ['ruta'] = 'Libretos'
        context ['encabezado'] = 'Libretos'
        return context
    