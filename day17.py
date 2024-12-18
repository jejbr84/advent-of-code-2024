import itertools
import math
import re
import numpy
from pprint import pprint
import functools
import sys


def main():
    with open('day17-input.txt') as file:
        lines = file.readlines()

    reg_A = int(lines[0].split(':')[1].strip())
    reg_B = int(lines[1].split(':')[1].strip())
    reg_C = int(lines[2].split(':')[1].strip())
    program = list(map(int, lines[4].split(':')[1].strip().split(',')))
    output = run([reg_A, reg_B, reg_C], program)
    print(f'Output: {','.join(map(str, output))}')


def run(registers, program):
    instruction_pointer = 0
    output = []
    iterations = 0
    while True:
        iterations += 1
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        if opcode == 0:  # adv
            registers[0] //= (2 ** combo_operand(operand, registers))
        elif opcode == 1: # bxl
            registers[1] ^= operand
        elif opcode == 2: # bst
            registers[1] = combo_operand(operand, registers) % 8
        elif opcode == 3: # jnz
            if registers[0] != 0:
                instruction_pointer = operand - 2 # later +2
        elif opcode == 4: # bxc
            registers[1] ^= registers[2]
        elif opcode == 5: # out
            output.append(combo_operand(operand, registers) % 8)
        elif opcode == 6: # bdv
            registers[1] = registers[0] // (2 ** combo_operand(operand, registers))
        elif opcode == 7: # cdv
            registers[2] = registers[0] // (2 ** combo_operand(operand, registers))

        instruction_pointer += 2
        if instruction_pointer >= len(program):
            break

    print(f'Iterations: {iterations}')

    return output


def combo_operand(literal_operand, registers):
    if literal_operand < 4:
        return literal_operand
    if literal_operand < 7:
        return registers[literal_operand - 4]
    print("Invalid combo operand")
    exit(1)


if __name__ == "__main__":
    main()
