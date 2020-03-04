from util.generator import World
from adventure.models import Player, Room

Room.objects.all().delete()

world = World()
world.generate_rooms()
