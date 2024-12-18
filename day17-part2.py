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

    reg_A = 180000000
    reg_B = int(lines[1].split(':')[1].strip())
    reg_C = int(lines[2].split(':')[1].strip())
    program = list(map(int, lines[4].split(':')[1].strip().split(',')))

    while True:
        output = run([reg_A, reg_B, reg_C], program)
        if output == program:
            break

        reg_A += 1
        if reg_A % 10000 == 0:
            print(f'Iteration: {reg_A}')

    print(f'Register A: {reg_A}')


def run(registers, program):
    instruction_pointer = 0
    output = []
    while True:
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        match opcode:
            case 0:
                registers[0] //= (2 ** combo_operand(operand, registers))
            case 1:
                registers[1] ^= operand
            case 2:
                registers[1] = combo_operand(operand, registers) % 8
            case 3:
                if registers[0] != 0:
                    instruction_pointer = operand - 2  # later +2
            case 4:
                registers[1] ^= registers[2]
            case 5:
                output.append(combo_operand(operand, registers) % 8)
                if output[-1] != program[len(output) - 1]:
                    break
            case 6:
                registers[1] = registers[0] // (2 ** combo_operand(operand, registers))
            case 7:
                registers[2] = registers[0] // (2 ** combo_operand(operand, registers))

        instruction_pointer += 2
        if instruction_pointer >= len(program):
            break

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

# Tot 180.000.000 getest
