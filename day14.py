import itertools
import math
import re
import numpy
from pprint import pprint
import functools


def main():
    with open('day14-input.txt') as file:
        lines = file.readlines()

    size = list(map(int, lines.pop(0).split(',')))
    size.reverse()

    robots_p = []
    robots_v = []
    for line in lines:
        p_and_v = line.split(' ')
        p = p_and_v[0].split('=')[1]
        robot_p = list(map(int, p.split(',')))
        robot_p.reverse()
        robots_p.append(robot_p)
        v = p_and_v[1].split('=')[1]
        robot_v = list(map(int, v.split(',')))
        robot_v.reverse()
        robots_v.append(robot_v)

    seconds = 100
    for robot in range(0, len(robots_p)):
        robot_p = robots_p[robot]
        robot_v = robots_v[robot]
        robot_p_raw = numpy.array(robot_p) + seconds * numpy.array(robot_v)
        robot_p[0] = wrap(robot_p_raw[0], size[0])
        robot_p[1] = wrap(robot_p_raw[1], size[1])

    # print([(robot[0].tolist(),robot[1].tolist()) for robot in robots_p])

    robot_count = numpy.zeros(size, dtype=int)
    for robot in robots_p:
        robot_count[tuple(robot)] += 1

    print(robot_count)

    height = size[0]
    width = size[1]
    q1 = numpy.sum(robot_count[0:height // 2, 0:width // 2])
    q2 = numpy.sum(robot_count[0:height // 2, width // 2 + 1:width])
    q3 = numpy.sum(robot_count[height // 2 + 1:height, 0:width // 2])
    q4 = numpy.sum(robot_count[height // 2 + 1:height, width // 2 + 1:width])
    safety_factor = q1 * q2 * q3 * q4

    print(f'Safety factor is {safety_factor}')


def wrap(number, maximum):
    if number >= 0:
        return number % maximum

    number_mod = -number % maximum
    if number_mod == 0:
        return number_mod

    return maximum - number_mod


if __name__ == "__main__":
    main()

# 26630 too high
# 26116 too high
# 25865 too low
