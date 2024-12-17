import itertools
import re
import numpy
from pprint import pprint
import functools


def main():
    with open('day09-input.txt') as file:
        line = file.readline()

    blocks = []
    file = True
    id = 0
    for digit in line.strip():
        digit = int(digit)
        if file:
            for _ in range(0, digit):
                blocks.append(id)
            id += 1
        else:
            for _ in range(0, digit):
                blocks.append('.')
        file = not file

    compacting = True
    end_index = len(blocks) - 1
    free_index = 0
    while compacting:
        while free_index < end_index:
            if blocks[free_index] == '.':
                break
            else:
                free_index += 1

        while free_index < end_index:
            if blocks[end_index] == '.':
                end_index -= 1
            else:
                break

        if free_index < end_index:
            blocks[free_index] = blocks[end_index]
            blocks[end_index] = '.'
            free_index += 1
            end_index -= 1
        else:
            compacting = False

    checksum = sum([index * id for index, id in enumerate(blocks) if id != '.'])
    print(checksum)


if __name__ == "__main__":
    main()
