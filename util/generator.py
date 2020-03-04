from util.content_gen import generateRooms
from random import randint
from adventure.models import Room

ROOMS = generateRooms()


class World:
    def __init__(self):
        self.grid = []

    def generate_rooms(self):
        grid = [[None] * 10 for _ in range(10)]
        room_count = 0

        for row in range(len(grid)):
            for room in range(len(grid[row])):
                grid[row][room] = Room(
                    title=ROOMS[room_count]['title'], description=ROOMS[room_count]['description'])
                grid[row][room].save()
                room_count += 1

        self.grid = grid

        for y, row in enumerate(self.grid):
            for x, room in enumerate(row):
                directions = ['n', 'w']
                direction = None
                if y - 1 < 0 and x - 1 < 0:
                    pass
                elif y - 1 < 0:
                    direction = "w"
                elif x - 1 < 0:
                    direction = "n"
                else:
                    rand_direction = randint(0, 1)
                    direction = directions[rand_direction]

                if direction == "w":
                    complement = self.grid[y][x - 1]
                    room.connectRooms(complement, direction)
                elif direction == "n":
                    complement = self.grid[y - 1][x]
                    room.connectRooms(complement, direction)
