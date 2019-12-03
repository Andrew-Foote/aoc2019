from collections import defaultdict
from dataclasses import dataclass
import itertools as it

@dataclass
class Vector:
    x: int
    y: int

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __abs__(self):
        return abs(self.x) + abs(self.y)

unit_vectors = {
    'R': Vector(1, 0),
    'D': Vector(0, -1),
    'L': Vector(-1, 0),
    'U': Vector(1, 0),
}

def parse_wire(src):
    return [(unit_vectors[token[0]], int(token[1:])) for token in src.split(',')]

def path(wire):
    pos = Vector(0, 0)

    for direction, magnitude in wire:        
        for _ in range(magnitude):
            pos += direction
            yield pos

def first_intersection(wire1, wire2):
    path1 = path(wire1)
    path2 = path(wire2)
    visitors = defaultdict(lambda: set())

    for pos1, pos2 in it.zip_longest(path1, path2):
        visitors[pos1].add(1)
        visitors[pos2].add(2)

        if len(visitors[pos1]) == 2:
            return abs(pos1)

        if len(visitors[pos2]) == 2:
            return abs(pos1)

with open('inputs/3.txt') as f:
    wire1, wire2 = map(parse_wire, f)

print(first_intersection(wire1, wire2))