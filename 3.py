from dataclasses import dataclass

@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __rmul__(self, scalar):
        return Vector(scalar * self.x, scalar * self.y)

    def __truediv__(self, scalar):
        return (1 / scalar) * self

    def __abs__(self):
        return abs(self.x) + abs(self.y)

    def unit(self):
        return self / abs(self)

def path(wire):
    pos = Vector(0, 0)

    for vector in wire:        
        for _ in range(abs(vector)):
            pos += vector.unit()
            yield pos

unit_vectors = {
    'R': Vector(1, 0),
    'D': Vector(0, -1),
    'L': Vector(-1, 0),
    'U': Vector(0, 1),
}

def parse_wire(wire):
    return [int(token[1:]) * unit_vectors[token[0]] for token in wire.split(',')]

with open('inputs/3.txt') as f:
    wire1, wire2 = map(parse_wire, f)

print(min(map(abs, set(path(wire1)) & set(path(wire2)))))