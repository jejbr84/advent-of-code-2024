import pprint

with open('day02-input.txt') as file:
    lines = file.readlines()

records = [[int(level.strip()) for level in line.split()] for line in lines]
record_diffs = [[level2 - level1 for level1, level2 in zip(record[:-1], record[1:])] for record in records]
safe_count = 0
for diffs in record_diffs:
    first_diff = diffs[0]
    for diff in diffs:
        if first_diff * diff <= 0 or abs(diff) > 3:
            break
    else:
        safe_count += 1

print(f'Safe count is {safe_count}')


# Part 2
def is_safe(diffs):
    first_diff = diffs[0]
    for diff in diffs:
        if first_diff * diff <= 0 or abs(diff) > 3:
            return False

    return True


safe_count = 0
unsafe_diffs = []
for diffs in record_diffs:
    if is_safe(diffs):
        safe_count += 1
    else:
        unsafe_diffs.append(diffs)

for diffs in unsafe_diffs:
    for index in range(-1, len(diffs)):
        diffs_reduced = diffs.copy()
        if index == len(diffs)-1:
            diffs_reduced = diffs_reduced[0:-1]
        elif index == -1:
            diffs_reduced = diffs_reduced[1:]
        else:
            diffs_reduced[index + 1] = diffs_reduced[index] + diffs_reduced[index + 1]
            del diffs_reduced[index]

        if is_safe(diffs_reduced):
            safe_count += 1
            break

print(f'Safe count is {safe_count}')
