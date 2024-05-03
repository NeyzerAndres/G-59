from django.urls import path
from . import views

app_name = "chat_app"

urlpatterns = [
    path('',views.AreasListView.as_view(), name= 'home'),
    path('',views.AreasTemplateView.as_view(), name= 'home'),
]