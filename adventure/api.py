from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))


@csrf_exempt
@api_view(["GET"])
def initialize(request):
    print(request)
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    start_room = Room.objects.get(n_to=0, w_to=0)
    player.currentRoom = start_room.id
    player.save()
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name': player.user.username, 'title': room.title, 'description': room.description, 'players': players}, safe=True)


@csrf_exempt
@api_view(["GET"])
def rooms(request):
    return JsonResponse(list(Room.objects.all().values("id", 'title', 'description', "n_to", "s_to", "e_to", "w_to")), safe=False, status=200)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    player = request.user.player
    player_id = player.id
    data = json.loads(request.body)

    roomId = data['newId']
    nextRoom = Room.objects.get(id=roomId)
    player.currentRoom = roomId
    player.save()
    players = nextRoom.playerNames(player_id)
    return JsonResponse({'name': player.user.username, 'title': nextRoom.title, 'description': nextRoom.description, 'players': players, 'error_msg': ""}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error': "Not yet implemented"}, safe=True, status=500)
