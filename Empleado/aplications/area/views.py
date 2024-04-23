from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


class AreaTemplateView(ListView):
    template_name = 'personal/reset_password_complete.html'
 