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
                directions = ['n', 's', 'e', 'w']

                if y - 1 < 0:
                    directions.remove('n')
                if y + 1 > len(self.grid) - 1:
                    directions.remove('s')
                if x - 1 < 0:
                    directions.remove('w')
                if x + 1 > len(row) - 1:
                    directions.remove('e')

                last_rand = None
                for _ in range(2):
                    idx = randint(0, len(directions) - 1)

                    while idx == last_rand:
                        idx = randint(0, len(directions) - 1)

                    direction = directions[idx]
                    if direction == 'n':
                        complement = self.grid[y - 1][x]
                    elif direction == 'e':
                        complement = self.grid[y][x + 1]
                    elif direction == 'w':
                        complement = self.grid[y][x - 1]
                    elif direction == 's':
                        complement = self.grid[y + 1][x]

                    room.connectRooms(complement, direction)
                    last_rand = idx
