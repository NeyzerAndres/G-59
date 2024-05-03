from django.shortcuts import render
from django.views.generic  import ListView
from django.http import HttpResponseForbidden
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
# class AreasListView(ListView):
#     template_name = 'chat/home.html'
#     model = models.Room
#     context_object_name = 'rooms'

def home(request):
    rooms = models.Room.objects.all()
    return render(request, 'chat/home.html', {'rooms': rooms})


@login_required
def room(request,room_id):
    try:
        room = request.user.rooms_joined.get(id=room_id)
    # rooms = models.Room.objects.all()
    # return render(request, 'chat/home.html', {'rooms': rooms})
    except models.Room.DoesNoExist:
        return HttpResponseForbidden()
    
    return


# class AreaTemplateView(CreateView):
#     template_name = "chat/rooms.html"
#     model = models.Room
#     context_object_name = 'rooms'

    



