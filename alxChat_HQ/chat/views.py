from curses import REPORT_MOUSE_POSITION
from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    """returns homepage"""

    return render(request, 'home.html')

def room(request, room ):
    """creates a chatroom"""

    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username':username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    """send and receive data on chat pagej"""

    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    """send messages to database"""

    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully fam :)')
    
def getMessages(request, room):
    """send messages to chat page"""

    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
