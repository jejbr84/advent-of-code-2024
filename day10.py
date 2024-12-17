import itertools
import re
import numpy
from pprint import pprint
import functools


def main():
    with open('day10-input.txt') as file:
        lines = file.readlines()

    hill_map = numpy.array([list([int(pos) for pos in line.strip()]) for line in lines])
    # print(hill_map)

    size = len(hill_map)
    trail_heads = []
    for ri in range(0, size):
        for ci in range(0, size):
            if hill_map[ri][ci] == 0:
                trail_heads.append((ri, ci))

    # print(trail_heads)

    all_trail_ends = []
    for trail_head in trail_heads:
        trail_ends = []
        trail_nexts = [trail_head]
        while len(trail_nexts) > 0:
            trail_current = trail_nexts.pop()
            height = hill_map[trail_current]
            trail_next = numpy.array(trail_current) + (1, 0)
            process_next(hill_map, height, size, trail_next, trail_nexts, trail_ends)
            trail_next = numpy.array(trail_current) + (-1, 0)
            process_next(hill_map, height, size, trail_next, trail_nexts, trail_ends)
            trail_next = numpy.array(trail_current) + (0, 1)
            process_next(hill_map, height, size, trail_next, trail_nexts, trail_ends)
            trail_next = numpy.array(trail_current) + (0, -1)
            process_next(hill_map, height, size, trail_next, trail_nexts, trail_ends)

        # print(trail_ends)
        all_trail_ends.append(trail_ends)

    score_sum = sum([len(set(trail_end)) for trail_end in all_trail_ends])
    print(f'Score sum is {score_sum}')

    # Part 2
    score_sum = sum([len(trail_end) for trail_end in all_trail_ends])
    print(f'Score sum is {score_sum}')


def process_next(hills, height, size, next, nexts, ends):
    if next.min() >= 0 and next.max() < size:
        next = tuple(next)
        if hills[next] == height + 1:
            if hills[next] == 9:
                ends.append(next)
            else:
                nexts.append(next)



if __name__ == "__main__":
    main()
