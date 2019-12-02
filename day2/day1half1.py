#!/usr/bin/env python3
import sys


def run(program):
    pc = 0
    while True:
        opcode = program[pc]

        if opcode == 1:
            a = program[program[pc+1]]
            b = program[program[pc+2]]
            program[program[pc+3]] = a + b
        elif opcode == 2:
            a = program[program[pc+1]]
            b = program[program[pc+2]]
            program[program[pc+3]] = a * b
        elif opcode == 99:
            break
        else:
            raise ValueError

        pc += 4

    return program


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f"usage: {__file__} <inputfile>")
        sys.exit(0)

    program = []
    with open(sys.argv[1], "r") as handle:
        text = handle.read()
        program = [int(token) for token in text.split(',')]

    if not sys.argv[1].startswith("test"):
        program[1] = 12
        program[2] = 2

    print(f"program: {program}")

    result = run(program)

    print(f"result: {result}")

