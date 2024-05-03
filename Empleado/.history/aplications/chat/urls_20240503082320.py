from django.urls import path
from . import views

app_name = "chat_app"

urlpatterns = [
    path('',views.home, name= 'home'),
    path('room/<pk>/',views.room, name= 'room'),
    # path('area/<pk>',views.AreaTemplateView.as_view(), name= 'area'),
]