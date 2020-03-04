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
                connected = False
                if y - 1 < 0:
                    directions.remove('n')
                if y + 1 > len(self.grid) - 1:
                    directions.remove('s')
                if x - 1 < 0:
                    directions.remove('w')
                if x + 1 > len(row) - 1:
                    directions.remove('e')
                while not connected:
                    for direction in directions:
                        neighbor = ''
                        if direction == 'n':
                            neighbor = self.grid[y + 1][x]
                        if direction == 'e':
                            neighbor = self.grid[y][x + 1]
                        if direction == 'w':
                            neighbor = self.grid[y][x - 1]
                        if direction == 's':
                            neighbor = self.grid[y - 1][x]
                        flag = randint(0, 1)
                        if flag:
                            room.connectRooms(neighbor, direction)
                            connected = True
        return self.grid
