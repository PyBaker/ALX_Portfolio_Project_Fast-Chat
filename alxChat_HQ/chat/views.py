from unicodedata import name
from django.shortcuts import redirect, render
from chat.models import Room, Message
# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request, room ):
    return render(request, 'room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
