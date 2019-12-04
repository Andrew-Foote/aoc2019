def path(wire):
    position = 0

    for vector in wire:
        magnitude = round(abs(vector))
        direction = vector / magnitude        
        for _ in range(magnitude):
            position += direction
            yield position

def manhattan_abs(vector):
    return abs(vector.real) + abs(vector.imag)

unit_vectors = {
    'R': 1,
    'D': -1j,
    'L': -1,
    'U': 1j,
}

def parse_wire(wire):
    return [int(token[1:]) * unit_vectors[token[0]] for token in wire.split(',')]

wire1, wire2 = map(parse_wire, open('inputs/3.txt'))
print(min(round(manhattan_abs(position)) for position in set(path(wire1)) & set(path(wire2))))