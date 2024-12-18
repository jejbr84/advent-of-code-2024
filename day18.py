import itertools
import math
import re
import numpy
from pprint import pprint
import functools
import sys
import copy

# [N, E, S, W]
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def main():
    with open('day18-input.txt') as file:
        lines = file.readlines()

    size = int(lines.pop(0).strip())
    nr_first_bytes = int(lines.pop(0).strip())

    memory_space = numpy.full((size, size), '.')
    start_pos = (0, 0)
    end_pos = (size - 1, size - 1)
    bytes = [tuple(map(int, line.strip().split(','))) for line in lines]

    for byte in bytes[0:nr_first_bytes]:
        memory_space[byte] = '#'

    pprint(numpy.transpose(memory_space))
    steps = find_shortest_path_to_end(memory_space, start_pos, end_pos)
    print(f'Steps is {steps}')

    # Part 2
    memory_space_init = copy.deepcopy(memory_space)
    min_index = nr_first_bytes
    max_index = len(bytes) - 1
    bisecting = True
    while bisecting:
        bisect_index = (min_index + max_index) // 2
        memory_space = copy.deepcopy(memory_space_init)
        for byte in bytes[nr_first_bytes:bisect_index + 1]:
            memory_space[byte] = '#'

        steps = find_shortest_path_to_end(memory_space, start_pos, end_pos)
        print(f'Byte index = {bisect_index}, byte = {bytes[bisect_index]}, steps = {steps}')
        if steps == sys.maxsize:
            max_index = bisect_index
        else:
            min_index = bisect_index

        if max_index - min_index == 1:
            bisecting = False


def find_shortest_path_to_end(memory_space, start_pos: tuple, end_pos: tuple):
    # Dijkstra to the rescue once again.
    steps_map = numpy.full((numpy.size(memory_space, 0), numpy.size(memory_space, 1)), sys.maxsize)
    unvisited_set = dict()
    reached_end = False
    for row in range(len(memory_space)):
        for column in range(len(memory_space[0])):
            if memory_space[row][column] != '#':
                unvisited_set[(row, column)] = sys.maxsize

    current_node = start_pos
    # Start with 0 steps.
    steps_map[start_pos] = 0
    while end_pos in unvisited_set:
        process_node(memory_space, current_node, steps_map, unvisited_set)

        # Select next node: the one with the smallest distance among the unvisited nodes.
        if len(unvisited_set) > 0:
            next_unvisited = min(unvisited_set.items(), key=lambda item: item[1])
            if next_unvisited[1] == sys.maxsize:
                break
            else:
                current_node = next_unvisited[0]

    if end_pos not in unvisited_set:
        reached_end = True

    return steps_map[end_pos] if reached_end else sys.maxsize


def process_node(memory_space, position: tuple, steps_map, unvisited_set: dict):
    score_at_node = steps_map[position]
    if score_at_node == sys.maxsize:
        unvisited_set.pop(position)
        return

    for move in MOVES:
        next_node = tuple(numpy.array(position) + move)
        if 0 <= next_node[0] < numpy.size(memory_space, 0) and 0 <= next_node[1] < numpy.size(memory_space, 1):
            if next_node in unvisited_set:
                # Next node is not visited yet.
                current_best = steps_map[next_node]
                new_score = score_at_node + 1
                if new_score < current_best:
                    # Found a better path to node, assign the score.
                    steps_map[next_node] = new_score
                    unvisited_set[next_node] = new_score

    # Done with node, mark as visited.
    unvisited_set.pop(position)


if __name__ == "__main__":
    main()

# 541 too high
