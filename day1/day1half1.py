#!/usr/bin/env python3
from math import floor
import sys


def fuel_for_mass(mass):
    return floor(mass / 3) - 2


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(f"usage: {__file__} <inputfile>\n\nTests:")
    
        for x in (12, 14, 1969, 100756):
            print(f"- mass {x} requires {fuel_for_mass(x)} fuel")

    else:
        fuel = 0
        with open(sys.argv[1], "r") as handle:
            for mass in handle.readlines():
                fuel += fuel_for_mass(int(mass))

        print(f"result: {fuel}")
