import pprint

with open('day01-input.txt') as file:
    lines = file.readlines()

left_list = []
right_list = []
for line in lines:
    [item1, item2] = line.split('   ')
    left_list.append(int(item1.strip()))
    right_list.append(int(item2.strip()))

left_list.sort()
right_list.sort()

total_distance = 0
for index in range(0, len(left_list)):
    distance = abs(left_list[index] - right_list[index])
    total_distance += distance

print(f'Distance is {total_distance}')

# Part 2

similarity_score = 0
for index in range(0, len(left_list)):
    number = left_list[index]
    multiplicity = right_list.count(number)
    similarity_score += number * multiplicity

print(f'Similarity score is {similarity_score}')
