from unicodedata import name
from django.urls import path

from chat.models import Room
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<str:room>/', views.room, name="room"),
    path('checkview', views.checkview, name='checkview')
]
