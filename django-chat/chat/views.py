from django.http import JsonResponse
from django.shortcuts import render
from chat import models
from django.contrib.auth.decorators import login_required


def rooms(request):
    return render(
        request, "chat/home.html", context={"rooms": models.Room.objects.all()}
    )


@login_required
def room(request, slug):
    room_obj = models.Room.objects.get(slug=slug)
    return render(
        request,
        "chat/room.html",
        context={
            "room": room_obj,
            "messages": models.Message.objects.filter(room=room_obj)[:25]
        }
    )
