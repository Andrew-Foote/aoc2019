from dataclasses import dataclass

def intersect(iterable1, iterable2, dupe_key, combiner):
    s = set(map(dupe_key, iterable1))

    for i in iterable2:
        if dupe_key(i) in s:
            yield i

def dedupe(iterable, dupe_key, sort_key):
    r = []
    ls = sorted(iterable, key=sort_key)

    last = dupe_key(ls[0])
    for i in ls[1:]:
        key = dupe_key(i)
        if key != last:
            r.append(i)
            last = key

    return r

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

path1 = enumerate(path(wire1))
path2 = enumerate(path(wire2))
isect = intersect(path1, path2, lambda pos, i: pos)


print(min(map(abs, set(path(wire1)) & set(path(wire2)))))