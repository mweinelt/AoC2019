#!/usr/bin/env python3
import sys
from typing import List
from functools import partial
from collections import namedtuple


Point = namedtuple("Point", "x y")


def manhattan_distance(a: Point, b: Point) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


distance_to_core = partial(manhattan_distance, Point(0, 0))


def points_in_path(path: List[str]) -> List[Point]:
    position = Point(0, 0)
    points = []
    for item in path:
        direction = item[0]
        steps = int(item.lstrip("UDLR"))

        if direction == "U":
            for i in range(steps):
                position = Point(position.x, position.y + 1)
                points.append(position)

        elif direction == "D":
            for i in range(steps):
                position = Point(position.x, position.y - 1)
                points.append(position)

        elif direction == "L":
            for i in range(steps):
                position = Point(position.x - 1, position.y)
                points.append(position)

        elif direction == "R":
            for i in range(steps):
                position = Point(position.x + 1, position.y)
                points.append(position)

        else:
            raise ValueError("illegal direction {direction}")

    return points


def intersections_in_points(a: List[Point], b: List[Point]) -> List[Point]:
    return set(a) & set(b)


def minimal_core_distance_from_points(points: List[Point]) -> int:
    return min(map(distance_to_core, points))


def minimal_wire_length_from_points(points: List[Point], path_a: List[Point], path_b: List[Point]) -> int:
    minimum = len(path_b) + len(path_a)
    for point in points:
        steps_a = path_a.index(point) + 1
        steps_b = path_b.index(point) + 1
        #print(point, steps_a, steps_b)

        if minimum and steps_a + steps_b < minimum:
            minimum = steps_a + steps_b
            #print(f"new minimum is {minimum} ({steps_a} + {steps_b}) for intersection {point}")

    return minimum


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f"usage: {__file__} <inputfilename>\n")

        examples = [
            ("R8,U5,L5,D3",
             "U7,R6,D4,L4"),
            ("R75,D30,R83,U83,L12,D49,R71,U7,L72",
             "U62,R66,U55,R34,D71,R55,D58,R83"),
            ("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
             "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
        ]

        for a, b in examples:
            intersections = intersections_in_points(
                    points_in_path(a.split(',')),
                    points_in_path(b.split(',')),
            )
            print(f"path {a} and {b} have closest intersection at distance {minimal_core_distance_from_points(intersections)}", end=' ')
            print(f"with intersections at {intersections}")

    else:
        wires = []
        with open(sys.argv[1], "r") as handle:
            for wire in handle.readlines():
                wires.append(wire)

        path_a = points_in_path(wires[0].strip().split(','))
        path_b = points_in_path(wires[1].strip().split(','))
        intersections = intersections_in_points(path_a, path_b)

        distance = minimal_core_distance_from_points(intersections)

        print(f"the input paths have their closest intersection at distance {distance}.")

        minimal_wire_distance = minimal_wire_length_from_points(intersections, path_a, path_b)

        print(f"the minimal amount of steps from both wires to an intersection is {minimal_wire_distance}")

