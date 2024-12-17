import re
import numpy
from pprint import pprint
import functools


def calculate(number, try_index):
    if len(number) == 1:
        return number[0]
    elif try_index % 2 == 0:
        # Addition
        new_number = number[1:]
        new_number[0] = number[0] + number[1]
        return calculate(new_number, try_index // 2)
    else:
        # Multiplication
        new_number = number[1:]
        new_number[0] = number[0] * number[1]
        return calculate(new_number, try_index // 2)


def main():
    with open('day07-input.txt') as file:
        lines = file.readlines()

    sums = []
    numbers = []
    for line in lines:
        parts = line.split(':')
        sums.append(int(parts[0]))
        numbers.append([int(number) for number in parts[1].strip().split()])

    total_sum = 0
    for sum, number in zip(sums, numbers):
        for try_index in range(0, pow(2, (len(number) - 1))):
            result = calculate(number, try_index)
            if result == sum:
                total_sum += sum
                break

    print(f'Total calibration result: {total_sum}')


if __name__ == "__main__":
    main()
