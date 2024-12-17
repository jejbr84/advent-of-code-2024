import itertools
import re
import numpy
from pprint import pprint
import functools


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None


max_val = 0


def main():
    with open('day11-sample-input.txt') as file:
        line = file.readline()

    arrangement_list = [int(number.strip()) for number in line.split()]
    arrangement = SLinkedList()
    arrangement.headval = Node(arrangement_list[0])
    previous_node = arrangement.headval
    for i in range(1, len(arrangement_list)):
        new_node = Node(arrangement_list[i])
        previous_node.nextval = new_node
        previous_node = new_node

    for _ in range(0, 25):
        blink(arrangement)
        print(max_val)

    print(f'Stones: {count_nodes(arrangement)}')

    # Part 2
    for i in range(0, 75):
        blink(arrangement)
        print(f'Arrangement {i + 1}')
        print(max_val)

    print(f'Stones: {count_nodes(arrangement)}')


def blink(arrangement: SLinkedList):
    global max_val
    node = arrangement.headval
    while node is not None:
        if node.dataval == 0:
            node.dataval = 1
        else:
            number_text = str(node.dataval)
            length = len(number_text)
            if length % 2 == 0:
                node.dataval = int(number_text[0:length // 2])
                new_node = Node(int(number_text[length // 2:]))
                new_node.nextval = node.nextval
                node.nextval = new_node
                node = new_node
            else:
                node.dataval = node.dataval * 2024

        node = node.nextval
        if node is not None:
            max_val = max(node.dataval, max_val)


def count_nodes(arrangement: SLinkedList):
    count = 0
    node = arrangement.headval
    while node is not None:
        node = node.nextval
        count += 1
    return count


if __name__ == "__main__":
    main()
