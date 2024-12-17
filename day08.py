import itertools
import re
import numpy
from pprint import pprint
import functools


def main():
    with open('day08-input.txt') as file:
        lines = file.readlines()

    antenna_map = numpy.array([list(line.strip()) for line in lines])
    pprint(antenna_map)

    size = antenna_map.shape[0]
    antenna_dict = dict()
    for ri, row in enumerate(antenna_map):
        for ci, col in enumerate(row):
            if col != '.':
                if col in antenna_dict.keys():
                    antenna_dict[col].append((ri, ci))
                else:
                    antenna_dict[col] = [(ri, ci)]

    antinodes = set()
    for value in antenna_dict.values():
        combs = itertools.combinations(value, 2)
        for comb in combs:
            diff = numpy.array(comb[0]) - comb[1]
            antinode1 = comb[0] + diff
            antinode2 = comb[1] - diff
            if antinode1.max() < size and antinode1.min() >= 0:
                antinodes.add(tuple(antinode1))
            if antinode2.max() < size and antinode2.min() >= 0:
                antinodes.add(tuple(antinode2))

    print(f'Antinode amount: {len(antinodes)}')

    # Part 2

    antinodes = set()
    for value in antenna_dict.values():
        combs = itertools.combinations(value, 2)
        for comb in combs:
            antinodes.add(tuple(comb[0]))
            antinodes.add(tuple(comb[1]))
            diff = numpy.array(comb[0]) - comb[1]
            distance = 1
            while True:
                antinode1 = comb[0] + diff * distance
                if antinode1.max() < size and antinode1.min() >= 0:
                    antinodes.add(tuple(antinode1))
                    distance += 1
                else:
                    break

            distance = 1
            while True:
                antinode2 = comb[1] - diff * distance
                if antinode2.max() < size and antinode2.min() >= 0:
                    antinodes.add(tuple(antinode2))
                    distance += 1
                else:
                    break

    print(f'Antinode amount: {len(antinodes)}')


if __name__ == "__main__":
    main()
