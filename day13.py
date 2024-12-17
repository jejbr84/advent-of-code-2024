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
    prizes = [tuple([int(match) for match in re.findall(r'(?<==)[0-9]+', line)]) for line in lines[2::4]]

    total_cost = 0
    for machine in range(0, len(buttons_a)):
        button_a = buttons_a[machine]
        button_b = buttons_b[machine]
        prize = prizes[machine]
        ax_max = prize[0] // button_a[0]
        ay_max = prize[1] // button_a[1]
        a_max = min(ax_max, ay_max, 100)
        cost = math.inf
        for i in range(0, a_max + 1):
            ax = button_a[0] * i
            ay = button_a[1] * i
            bx = prize[0] - ax
            by = prize[1] - ay
            jx, jx_remain = divmod(bx, button_b[0])
            jy, jy_remain = divmod(by, button_b[1])
            if jx == jy and jx <= 100 and jx_remain == 0 and jy_remain == 0:
                # Found it. A is the most expensive, so the lowest A is the lowest total.
                cost = 3 * i + jx
                # print(f'Found prize {prize}, cost {cost}')
                break

        # print(f'Minimum cost {prize}, cost {cost_min}')
        if cost is not math.inf:
            total_cost += cost

    print(f'Total cost is {total_cost}')


if __name__ == "__main__":
    main()

# 26630 too high
# 26116 too high
# 25865 too low
