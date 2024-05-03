from django.shortcuts import render
from django.views.generic  import TemplateView,
class MODEL_NAMEListView(ListView):
    model = MODEL_NAME
    template_name = "TEMPLATE_NAME"

from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
class  


def home(request):
    rooms = models.Room.objects.all()
    return render(request, 'chat/home.html', {'rooms': rooms})
    




