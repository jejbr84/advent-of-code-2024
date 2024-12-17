import re
import numpy
from pprint import pprint
import functools

with open('day06-input.txt') as file:
    lines = file.readlines()

lab_map = numpy.array([list(line.strip()) for line in lines])

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
directions = [NORTH, EAST, SOUTH, WEST]

start_pos = (-1, -1)
for ri, row in enumerate(lab_map):
    for ci, col in enumerate(row):
        if col == '^':
            start_pos = numpy.array([ri, ci])

guard_pos = start_pos
direction_index = 0
running = True
while running:
    lab_map[guard_pos[0]][guard_pos[1]] = 'X'
    guard_pos += directions[direction_index]
    if (guard_pos[0] < 0 or guard_pos[0] >= len(lab_map) or
            guard_pos[1] < 0 or guard_pos[1] >= len(lab_map[0])):
        running = False
    next_guard_pos = guard_pos + directions[direction_index]

    if (next_guard_pos[0] < 0 or next_guard_pos[0] >= len(lab_map) or
            next_guard_pos[1] < 0 or next_guard_pos[1] >= len(lab_map[0])):
        pass
    elif lab_map[next_guard_pos[0]][next_guard_pos[1]] == '#':
        direction_index += 1
        direction_index %= len(directions)
    # pprint(lab_map)

distinct_pos = 0
for ri, row in enumerate(lab_map):
    for ci, col in enumerate(row):
        if col == 'X':
            distinct_pos += 1

print(f'Distinct posítions: {distinct_pos}')
