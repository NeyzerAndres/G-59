from django.shortcuts import render
from django.views.generic  import TemplateView,ListView,CreateView

from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
class AreasListView(ListView):
    template_name = 'chat/home.html'
    model = models.Room
    context_object_name = 'rooms'

# def home(request):
#     rooms = models.Room.objects.all()
#     return render(request, 'chat/home.html', {'rooms': rooms})
    


class AreaTemplateView(TemplateView):
    template_name = "chat/rooms.html"
    



