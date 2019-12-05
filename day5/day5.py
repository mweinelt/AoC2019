#!/usr/bin/env python3
import sys
from typing import List


def run(memory: List[int], override=None) -> List[int]:
    if override:
        for address, value in override:
            memory[address] = value

    address = 0
    while True:
        instruction = memory[address]
        opcode = int(str(instruction)[-2:]) if instruction >= 10 else instruction
        try:
            param1_immediate = int(str(instruction)[-3]) == 1
        except IndexError:
            param1_immediate = False

        try:
            param2_immediate = int(str(instruction)[-4]) == 1
        except IndexError:
            param2_immediate = False

        try:
            param3_immediate = int(str(instruction)[-5]) == 1
        except IndexError:
            param3_immediate = False


        print(f"{instruction} {opcode=}, {param1_immediate=}, {param2_immediate=}, {param3_immediate=}")

        if opcode == 1:
            a = memory[address+1] if param1_immediate else memory[memory[address+1]] 
            b = memory[address+2] if param2_immediate else memory[memory[address+2]]
            memory[memory[address+3]] = a + b
            address +=4
        elif opcode == 2:
            a = memory[address+1] if param1_immediate else memory[memory[address+1]] 
            b = memory[address+2] if param2_immediate else memory[memory[address+2]]
            memory[memory[address+3]] = a * b
            address +=4
        elif opcode == 3:
            memory[memory[address+1]] = int(input("#3: Input:\n"))
            address += 2
        elif opcode == 4:
            print(memory[address + 1 if param1_immediate else memory[address+1]])
            address += 2
        elif opcode == 5:
            a = memory[address + 1] if param1_immediate else memory[memory[address + 1]]
            if a != 0:
                address = memory[address+2] if param2_immediate else memory[memory[address + 2]]
            else:
                address += 3
        elif opcode == 6:
            a = memory[address + 1] if param1_immediate else memory[memory[address + 1]]
            if a == 0:
                address = memory[address+2] if param2_immediate else memory[memory[address + 2]]
            else:
                address += 3
        elif opcode == 7:
            a = memory[address+1] if param1_immediate else memory[memory[address+1]] 
            b = memory[address+2] if param2_immediate else memory[memory[address+2]]
            memory[memory[address+3]] = 1 if a < b else 0
            address += 4
        elif opcode == 8:
            a = memory[address+1] if param1_immediate else memory[memory[address+1]] 
            b = memory[address+2] if param2_immediate else memory[memory[address+2]]
            memory[memory[address+3]] = 1 if a == b else 0
            address += 4
        elif opcode == 99:
            break
        else:
            raise ValueError(f"unhandled opcode {opcode}")

    return memory


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f"usage: {__file__} <inputfile>")
        sys.exit(0)

    memory = []
    with open(sys.argv[1], "r") as handle:
        text = handle.read()
        memory = [int(token) for token in text.split(',')]

    run(memory)
