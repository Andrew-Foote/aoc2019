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

# we need each intersection along with the number of steps each wire takes to first get to that intersection

unit_vectors = {
    'R': 1,
    'D': -1j,
    'L': -1,
    'U': 1j,
}

def parse_wire(wire):
    return [int(token[1:]) * unit_vectors[token[0]] for token in wire.split(',')]

# inelegant but works
wire1, wire2 = (enumerate(path(parse_wire(wire))) for wire in open('inputs/3.txt'))
wire1_index = {}

for index, position in wire1:
    if position not in wire1_index:
        wire1_index[position] = index

wire2_index = {}
current_min = None

for index, position in wire2:
    if position not in wire2_index:
        if position in wire1_index:
            index_sum = wire1_index[position] + index

            if current_min is None or index_sum < current_min:
                current_min = index_sum

        wire2_index[position] = index

print(current_min + 2)