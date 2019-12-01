#!/usr/bin/env python3
from math import floor
import sys


def fuel_for_mass(mass: int) -> int:
    return floor(mass / 3) - 2


def fuel_for_fuel(mass: int) -> int:
    fuel = fuel_for_mass(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_for_fuel(fuel)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(f"usage: {__file__} <inputfile>\n\nTests:")

        for x in (12, 14, 1969, 100756):
            print(f"- mass {x} requires {fuel_for_mass(x)} fuel")

        for x in (14, 1969, 100756):
            print(f"- fuel {x} requires {fuel_for_fuel(x)} fuel")

    else:
        total_fuel = 0
        with open(sys.argv[1], "r") as handle:
            for mass in handle.readlines():
                module_fuel = fuel_for_mass(int(mass))
                total_fuel += module_fuel + fuel_for_fuel(module_fuel)

        print(f"result: {total_fuel}")
