from django.shortcuts import render
from django.views.generic  import ListView

from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
class AreasListView(ListView):
    template_name = 'chat/home.html'
    model = models.Room
    context_object_name = 'rooms'

def room(request):
    rooms = models.Room.objects.all()
    return render(request, 'chat/home.html', {'rooms': rooms})
    


# class AreaTemplateView(CreateView):
#     template_name = "chat/rooms.html"
#     model = models.Room
#     context_object_name = 'rooms'

    



