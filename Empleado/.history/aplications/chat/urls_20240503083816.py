from django.urls import path
from . import views

app_name = "chat_app"

urlpatterns = [
    path('',views.AreasListView.as_view(), name= 'home'),
    path('room/<int:room_id>/',views.room, name= 'room'),
    path('sin_acceso/',views.ErrorTemplateView, name= 'error404'),
    # path('area/<pk>',views.AreaTemplateView.as_view(), name= 'area'),
]