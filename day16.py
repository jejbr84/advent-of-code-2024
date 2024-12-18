import itertools
import math
import re
import numpy
from pprint import pprint
import functools
import sys

# [N, E, S, W]
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def main():
    with open('day16-input.txt') as file:
        lines = file.readlines()

    maze = []
    start_pos = ()
    end_pos = ()
    for line in lines:
        start_token = line.find('S')
        if start_token != -1:
            start_pos = (len(maze), start_token)

        end_token = line.find('E')
        if end_token != -1:
            end_pos = (len(maze), end_token)

        maze_row = list(line.strip())
        maze.append(maze_row)

    # pprint(maze)
    score, score_map = find_shortest_path_to_end(maze, start_pos, end_pos)
    print(f'Score is {score}')

    # Part 2
    tiles = find_tiles_on_best_paths(score_map, end_pos)
    print(f'Tiles are {tiles}')


def find_shortest_path_to_end(maze, start_pos: tuple, end_pos: tuple):
    # Use Dijkstra's algorithm.
    score_map = [[(sys.maxsize, -1)] * len(maze[0]) for _ in range(len(maze))]
    # Key is position tuple, value is (lowest score, direction index)
    unvisited_set = dict()
    reached_end = False
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            if maze[row][column] != '#':
                unvisited_set[(row, column)] = (sys.maxsize, -1)

    current_node = start_pos
    # Start with score 0 in east direction.
    score_map[start_pos[0]][start_pos[1]] = (0, 1)
    while end_pos in unvisited_set:
        process_node(maze, current_node, score_map, unvisited_set)

        # Select next node: the one with the smallest distance among the unvisited nodes.
        if len(unvisited_set) > 0:
            next_unvisited = min(unvisited_set.items(), key=lambda item: item[1][0])
            if next_unvisited[1] == sys.maxsize:
                break
            else:
                current_node = next_unvisited[0]
    else:
        reached_end = True

    return (score_map[end_pos[0]][end_pos[1]][0], score_map) if reached_end else (sys.maxsize, score_map)


def process_node(maze, position: tuple, score_map: list, unvisited_set: dict):
    row = position[0]
    column = position[1]
    score_at_node = score_map[row][column][0]
    if score_at_node == sys.maxsize:
        # print(f"Error, node {position} has no steps assigned yet")
        # exit(1)
        unvisited_set.pop(position)
        return

    # steps_map[row][column] = steps_to_node
    # height = ord(maze[row][column])
    direction_at_node = score_map[row][column][1]
    for direction_index in range(direction_at_node - 1, direction_at_node + 2):
        direction_index_wrapped = (direction_index + len(MOVES)) % len(MOVES)
        move = MOVES[direction_index_wrapped]
        next_row = row + move[0]
        next_column = column + move[1]
        if 0 <= next_row < len(maze) and 0 <= next_column < len(maze[0]):
            if (next_row, next_column) in unvisited_set:
                # Next node is not visited yet.
                current_best = score_map[next_row][next_column][0]
                new_score = score_at_node + 1 + 1000 * abs(direction_at_node - direction_index)
                if new_score < current_best:
                    # Found a better path to node, assign the score.
                    score_map[next_row][next_column] = (new_score, direction_index_wrapped)
                    unvisited_set[(next_row, next_column)] = (new_score, direction_index_wrapped)

    # Done with node, mark as visited.
    unvisited_set.pop(position)


def find_tiles_on_best_paths(score_map, end_pos: tuple) -> int:
    backtrace_set = {end_pos}
    best_path_tiles = {end_pos}
    previous_direction = None
    while backtrace_set:
        row, column = backtrace_set.pop()
        lowest_nodes = []
        current_score = score_map[row][column][0]
        for direction_index in range(len(MOVES)):
            move = MOVES[direction_index]
            back_row = row + move[0]
            back_column = column + move[1]
            back_score = score_map[back_row][back_column][0]
            if (back_score == current_score - 1 or back_score == current_score - 1001 or
                    (previous_direction is not None and score_map[row][column][1] != previous_direction and
                     back_score == current_score + 999)):
                lowest_nodes.append((back_row, back_column))

        if lowest_nodes:
            backtrace_set = backtrace_set | set(lowest_nodes)
            best_path_tiles = best_path_tiles | set(lowest_nodes)

        previous_direction = score_map[row][column][1]

    # pprint(best_path_tiles)
    return len(best_path_tiles)


if __name__ == "__main__":
    main()

# 541 too high
