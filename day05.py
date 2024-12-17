import re
import numpy
from pprint import pprint
import functools

with open('day05-input.txt') as file:
    lines = file.readlines()


def rule_compare(left, right):
    if rules.count((left, right)) > 0:
        return -1
    elif rules.count((right, left)) > 0:
        return 1
    else:
        return 0


rules = []
updates = []
is_rules = True
for line in lines:
    line = line.strip()
    if line == '':
        is_rules = False
        continue

    if is_rules:
        rule = line.split('|')
        rules.append((int(rule[0]), int(rule[1])))
    else:
        update = [int(page) for page in line.split(',')]
        updates.append(update)

middle_sum = 0
for update in updates:
    update_sorted = sorted(update, key=functools.cmp_to_key(rule_compare))
    if update == update_sorted:
        middle_sum += update[int(len(update)/2)]

print(f'Middle sum is {middle_sum}')

# Part 2

middle_sum = 0
for update in updates:
    update_sorted = sorted(update, key=functools.cmp_to_key(rule_compare))
    if update != update_sorted:
        middle_sum += update_sorted[int(len(update)/2)]

print(f'Middle sum is {middle_sum}')
