import itertools
import math
import re
import numpy
from pprint import pprint
import functools


def main():
    with open('day13-input.txt') as file:
        lines = file.readlines()

    buttons_a = [tuple([int(match) for match in re.findall(r'(?<=\+)[0-9]+', line)]) for line in lines[0::4]]
    buttons_b = [tuple([int(match) for match in re.findall(r'(?<=\+)[0-9]+', line)]) for line in lines[1::4]]
    prizes = [tuple([int(match) + 10000000000000 for match in re.findall(r'(?<==)[0-9]+', line)]) for line in
              lines[2::4]]

    total_cost = 0
    for machine in range(0, len(buttons_a)):
        button_a = buttons_a[machine]
        button_b = buttons_b[machine]
        prize = prizes[machine]

        i = ((prize[0] - (button_b[0] * prize[1] / button_b[1])) /
             (button_a[0] - (button_b[0] * button_a[1] / button_b[1])))

        if abs(round(i) - i) < 0.001 and round(i) >= 0:
            j = (prize[1] - button_a[1] * i) / button_b[1]
            if abs(round(j) - j) < 0.001 and round(j) >= 0:
                cost = int(round(3 * i + j))
                # print(f'Found prize {prize}, cost {cost}, A={i}, B={j}')
                total_cost += cost

    print(f'Total cost is {total_cost}')


if __name__ == "__main__":
    main()

#  54341070823689 too low
# 105620095782547 OK!
# 164327753564359 too high
# 165389116105951 too high
