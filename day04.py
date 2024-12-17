import re
import numpy
from pprint import pprint

with open('day04-input.txt') as file:
    lines = file.readlines()


def find_xmas(word_search_list):
    count = 0
    for row in word_search_list:
        row_text = ''.join(row)
        xmas_matches = re.findall('XMAS', row_text)
        count += len(xmas_matches)

        xmas_matches = re.findall('XMAS', row_text[::-1])
        count += len(xmas_matches)

    return count


def find_x_mas(word_search_list):
    count = 0
    for row in range(1, len(word_search_list) - 1):
        for column in range(1, len(word_search_list) - 1):
            # Zoek A, kijk dan naar één van de patronen. Rotaties van buitenaf
            if word_search_list[row][column] == 'A':
                if word_search_list[row - 1][column - 1] == 'M' and word_search_list[row - 1][column + 1] == 'M' and \
                        word_search_list[row + 1][column - 1] == 'S' and word_search_list[row + 1][column + 1] == 'S':
                    count += 1

    return count


word_search = numpy.array([list(line.strip()) for line in lines])
xmas_count = find_xmas(word_search.tolist())
xmas_count += find_xmas(word_search.transpose().tolist())

word_search_diag = []
width = len(word_search)
for i in range(-width + 1, width):
    word_search_diag.append(numpy.diag(word_search, i).tolist())
xmas_count += find_xmas(word_search_diag)

word_search_diag = []
for i in range(-width + 1, width):
    word_search_diag.append(numpy.diag(numpy.rot90(word_search), i).tolist())
xmas_count += find_xmas(word_search_diag)

print(f'XMAS count is {xmas_count}')

# Part 2

xmas_count = find_x_mas(word_search.tolist())
word_search = numpy.rot90(word_search)
xmas_count += find_x_mas(word_search.tolist())
word_search = numpy.rot90(word_search)
xmas_count += find_x_mas(word_search.tolist())
word_search = numpy.rot90(word_search)
xmas_count += find_x_mas(word_search.tolist())
print(f'X-MAS count is {xmas_count}')
