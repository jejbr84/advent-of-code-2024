import itertools
import math
import re
import sys

import numpy
from pprint import pprint
import functools
import copy


def main():
    with open('day14-input.txt') as file:
        lines = file.readlines()

    size = list(map(int, lines.pop(0).split(',')))
    size.reverse()

    robots_p_init = []
    robots_v = []
    for line in lines:
        p_and_v = line.split(' ')
        p = p_and_v[0].split('=')[1]
        robot_p = list(map(int, p.split(',')))
        robot_p.reverse()
        robots_p_init.append(robot_p)
        v = p_and_v[1].split('=')[1]
        robot_v = list(map(int, v.split(',')))
        robot_v.reverse()
        robots_v.append(robot_v)

    for seconds in range(100000):
        if seconds % 10000 == 0:
            print(seconds)

        robots_p = copy.deepcopy(robots_p_init)
        for robot in range(0, len(robots_p)):
            robot_p = robots_p[robot]
            robot_v = robots_v[robot]
            robot_p_raw = numpy.array(robot_p) + seconds * numpy.array(robot_v)
            robot_p[0] = wrap(robot_p_raw[0], size[0])
            robot_p[1] = wrap(robot_p_raw[1], size[1])

        # print([(robot[0].tolist(),robot[1].tolist()) for robot in robots_p])

        robot_present = numpy.zeros(size, dtype=int)
        for robot in robots_p:
            if robot_present[tuple(robot)] == 1:
                break
            else:
                robot_present[tuple(robot)] = 1
        else:
            print(f'X-mas tree after {seconds} seconds (all robots on unique positions:')
            print_robots(robot_present)
            break
    else:
        print(f'X-mas tree not found')


def wrap(number, maximum):
    if number >= 0:
        return number % maximum

    number_mod = -number % maximum
    if number_mod == 0:
        return number_mod

    return maximum - number_mod


def print_robots(robots):
    for row in robots:
        print(''.join(['X' if robot > 0 else ' ' for robot in row]))


if __name__ == "__main__":
    main()

# 278 too low
# 279 too low
