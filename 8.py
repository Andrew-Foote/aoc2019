digits = list(map(int, open('inputs/8.txt').read().strip()))

def layers(digits, width, height):
    column_count = 0
    row_count = 0
    layer = []

    for digit in digits:
        layer.append(digit)

        if column_count == width - 1:
            column_count = 0

            if row_count == height - 1:
                row_count = 0
                yield layer
                layer = []
            else:
                row_count += 1
        else:
            column_count += 1

layer = min(layers(digits, 25, 6), key=lambda layer: sum(1 for digit in layer if digit == 0))
print(sum(1 for digit in layer if digit == 1) * sum(1 for digit in layer if digit == 2))