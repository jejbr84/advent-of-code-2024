import re

with open('day03-input.txt') as file:
    lines = file.readlines()

mul_sum = 0
for line in lines:
    mul_pairs = re.findall('mul\((\d{1,3}),(\d{1,3})\)', line.strip())
    mul_sum += sum([int(mul_pair[0]) * int(mul_pair[1]) for mul_pair in mul_pairs])

print(mul_sum)

# Part 2

mul_sum = 0
enabled = True
for line in lines:
    mul_pairs = re.findall('mul\((\d{1,3}),(\d{1,3})\)|(don\'t\(\))|(do\(\))', line.strip())
    for mul_pair in mul_pairs:
        if len(mul_pair[2]) > 0:
            enabled = False
            continue
        if len(mul_pair[3]) > 0:
            enabled = True
            continue
        if enabled:
            mul_sum += int(mul_pair[0]) * int(mul_pair[1])

print(mul_sum)
