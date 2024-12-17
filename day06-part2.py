import re
import numpy
from pprint import pprint
import functools

with open('day06-input.txt') as file:
    lines = file.readlines()

lab_map_org = numpy.array([list(line.strip()) for line in lines])
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

guard_pos = start_pos.copy()
direction_index = 0
running = True
while running:
    lab_map_org[guard_pos[0]][guard_pos[1]] = 'X'
    guard_pos += directions[direction_index]
    if (guard_pos[0] < 0 or guard_pos[0] >= len(lab_map_org) or
            guard_pos[1] < 0 or guard_pos[1] >= len(lab_map_org[0])):
        running = False
    next_guard_pos = guard_pos + directions[direction_index]

    if (next_guard_pos[0] < 0 or next_guard_pos[0] >= len(lab_map_org) or
            next_guard_pos[1] < 0 or next_guard_pos[1] >= len(lab_map_org[0])):
        pass
    elif lab_map_org[next_guard_pos[0]][next_guard_pos[1]] == '#':
        direction_index += 1
        direction_index %= len(directions)

loop_positions = []
tries = 0
for ri in range(0, len(lab_map)):
    print(f'Row index is {ri}')
    for ci in range(0, len(lab_map[ri])):
        if lab_map[ri][ci] == '.' and lab_map_org[ri][ci] == 'X':
            lab_map[ri][ci] = '#'

            guard_pos = start_pos.copy()
            direction_index = 0
            turn_positions = []
            running = True
            tries += 1
            while running:
                # lab_map[guard_pos[0]][guard_pos[1]] = 'X'
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
                    if (guard_pos[0], guard_pos[1]) in turn_positions:
                        # Loop detected
                        running = False
                        loop_positions.append((ri, ci))
                    else:
                        turn_positions.append((guard_pos[0], guard_pos[1]))

                # pprint(lab_map)

            lab_map[ri][ci] = '.'

# loop_positions = set()
# size = len(lab_map)
# for ri in range(0, size):
#     print(f'Row index is {ri}')
#     for ci in range(0, len(lab_map[ri])):
#         if lab_map[ri][ci] == '#':
#             ri2 = ri + 1
#             if ri2 >= size:
#                 continue
#             for ci2 in range(ci + 1, len(lab_map[ri])):
#                 if lab_map[ri2][ci2] == '#':
#                     ci3 = ci2 - 1
#                     for ri3 in range(ri2 + 1, size):
#                         if lab_map[ri3][ci3] == '#':
#                             if lab_map_org[ri3 - 1][ci - 1] == 'X':
#                                 row = ri3 - 1
#                                 col = ci - 1
#                                 loop_positions.add((row, col))
#
# lab_map = numpy.rot90(lab_map)
# lab_map_org = numpy.rot90(lab_map_org)
# for ri in range(0, size):
#     print(f'Row index is {ri}')
#     for ci in range(0, len(lab_map[ri])):
#         if lab_map[ri][ci] == '#':
#             ri2 = ri + 1
#             if ri2 >= size:
#                 continue
#             for ci2 in range(ci + 1, len(lab_map[ri])):
#                 if lab_map[ri2][ci2] == '#':
#                     ci3 = ci2 - 1
#                     for ri3 in range(ri2 + 1, size):
#                         if lab_map[ri3][ci3] == '#':
#                             if lab_map_org[ri3 - 1][ci - 1] == 'X':
#                                 row = ci - 1
#                                 col = size - 1 - (ri3 - 1)
#                                 loop_positions.add((row, col))
#
# lab_map = numpy.rot90(lab_map)
# lab_map_org = numpy.rot90(lab_map_org)
# for ri in range(0, size):
#     print(f'Row index is {ri}')
#     for ci in range(0, len(lab_map[ri])):
#         if lab_map[ri][ci] == '#':
#             ri2 = ri + 1
#             if ri2 >= size:
#                 continue
#             for ci2 in range(ci + 1, len(lab_map[ri])):
#                 if lab_map[ri2][ci2] == '#':
#                     ci3 = ci2 - 1
#                     for ri3 in range(ri2 + 1, size):
#                         if lab_map[ri3][ci3] == '#':
#                             if lab_map_org[ri3 - 1][ci - 1] == 'X':
#                                 row = size - 1 - (ri3 - 1)
#                                 col = size - 1 - (ci - 1)
#                                 loop_positions.add((row, col))
#
# lab_map = numpy.rot90(lab_map)
# lab_map_org = numpy.rot90(lab_map_org)
# for ri in range(0, size):
#     print(f'Row index is {ri}')
#     for ci in range(0, len(lab_map[ri])):
#         if lab_map[ri][ci] == '#':
#             ri2 = ri + 1
#             if ri2 >= size:
#                 continue
#             for ci2 in range(ci + 1, len(lab_map[ri])):
#                 if lab_map[ri2][ci2] == '#':
#                     ci3 = ci2 - 1
#                     for ri3 in range(ri2 + 1, size):
#                         if lab_map[ri3][ci3] == '#':
#                             if lab_map_org[ri3 - 1][ci - 1] == 'X':
#                                 row = size - 1 - (ci - 1)
#                                 col = ri3 - 1
#                                 loop_positions.add((row, col))

print(f'Distinct posítions: {len(loop_positions)}')
# pprint(loop_positions)

# 1427 too low
# 3855 too high
