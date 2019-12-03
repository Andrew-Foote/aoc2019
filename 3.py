with open('inputs/3.txt') as f:
    wire1, wire2 = (line.split(',') for line in f)

unit_vectors = {
    'R': [1, 0],
    'D': [0, -1],
    'L': [-1, 0],
    'U': [1, 0],
}

def path(wire):
    pos = [0, 0]

    for vec_src in wire:
        direction = vec_src[0]
        magnitude = int(vec_src[1:])
        vec = unit_vectors[direction]
        
        for _ in range(magnitude):
            pos[0] += vec[0]
            pos[1] += vec[1]
            yield tuple(pos)

def find_intersection_point(wire1, wire2):
    path1 = set(path(wire1))
    path2 = path(wire2)

    for pos in path2:
        if pos in path1:
            return abs(pos[0]) + abs(pos[1])

print(find_intersection_point(wire1, wire2))