from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    chatrooms = Chatroom.objects.all()
    return render(request, "chat_app/index.html", {"chatrooms": chatrooms})


def chatroom(request, slug):
    room = Chatroom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=room)[0:30]
    return render(request, "chat_app/room.html", {"room": room, "messages": messages})


def about(request):
    return render(request, "chat_app/about.html")


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def room_view(request):
    user_profile_image = (
        request.user.profile.image.url if request.user.is_authenticated else None
    )
    return render(
        request,
        "chat_app/rooms.html",
        {
            "user_profile_image": user_profile_image,
        },
    )
