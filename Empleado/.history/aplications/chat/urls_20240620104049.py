from django.urls import path
from . import views

app_name = "chat_app"

urlpatterns = [
    path('',views.home, name= 'home'),
    path('room/<int:room_id>/',views.room, name= 'room'),
    path('sin_acceso/',views.ErrorTemplateView.as_view(), name= 'error404'),
    # path('area/<pk>',views.AreaTemplateView.as_view(), name= 'area'),
]