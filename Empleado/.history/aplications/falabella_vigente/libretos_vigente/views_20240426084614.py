from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Libreto31TemplateView(TemplateView):
    template_name = 'falabella_vigente/libretos/libreto31.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)