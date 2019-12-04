from dataclasses import dataclass

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

def path(wire):
    pos = Vector(0, 0)

    for direction, magnitude in wire:        
        for _ in range(magnitude):
            pos += direction
            yield pos

unit_vectors = {
    'R': Vector(1, 0),
    'D': Vector(0, -1),
    'L': Vector(-1, 0),
    'U': Vector(0, 1),
}

def parse_wire(src):
    return [(unit_vectors[token[0]], int(token[1:])) for token in src.split(',')]

with open('inputs/3.txt') as f:
    wire1, wire2 = map(parse_wire, f)

print(min(map(abs, set(path(wire1)) & set(path(wire2)))))