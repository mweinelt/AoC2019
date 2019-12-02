#!/usr/bin/env python3
import sys
from typing import List


def run(memory: List[int], override=None) -> List[int]:
    if override:
        for address, value in override:
            memory[address] = value

    address = 0
    while True:
        opcode = memory[address]

        if opcode == 1:
            a = memory[memory[address+1]]
            b = memory[memory[address+2]]
            memory[memory[address+3]] = a + b
        elif opcode == 2:
            a = memory[memory[address+1]]
            b = memory[memory[address+2]]
            memory[memory[address+3]] = a * b
        elif opcode == 99:
            break
        else:
            raise ValueError(f"unhandled opcode {opcode}")

        address += 4

    return memory


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f"usage: {__file__} <inputfile>")
        sys.exit(0)

    memory = []
    with open(sys.argv[1], "r") as handle:
        text = handle.read()
        memory = [int(token) for token in text.split(',')]

    print(f"memory: {memory}")

    for noun in range(100):
        for verb in range(100):
            try:
                result = run(memory.copy(), [(1, noun), (2, verb)])
            except ValueError:
                continue

            if result[0] == 19690720:
                print(f"noun: {noun}, verb: {verb}")
                print(f"result: {result}")
                sys.exit(0)

