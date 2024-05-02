from django.shortcuts import render
from django.views.generic  import TemplateView
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    rooms = models.Rooms.objects.all()
    




