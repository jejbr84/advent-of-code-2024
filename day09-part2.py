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

    id += 1
    end_index = len(blocks) - 1
    free_index = 0
    while end_index > 0:
        while end_index > 0:
            if blocks[end_index] == '.' or int(blocks[end_index]) >= id:
                end_index -= 1
            else:
                break

        file_size = 1
        id = blocks[end_index]
        while end_index > 0:
            if blocks[end_index - 1] == id:
                end_index -= 1
                file_size += 1
            else:
                break

        free_end_index = free_index
        fit_size = 0
        start_occupied = True
        while free_end_index < end_index and fit_size < file_size:
            if blocks[free_end_index + 1] == '.':
                fit_size += 1
                start_occupied = False
            else:
                fit_size = 0
                if start_occupied:
                    free_index += 1
            free_end_index += 1

        if fit_size == file_size:
            for i in range(0, file_size):
                blocks[free_end_index - file_size + 1 + i] = blocks[end_index + i]
                blocks[end_index + i] = '.'

        end_index -= 1

    checksum = sum([index * id for index, id in enumerate(blocks) if id != '.'])
    print(checksum)


if __name__ == "__main__":
    main()
