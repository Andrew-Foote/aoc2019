import sys

def digits(n):
    while n > 0:
        yield n % 10
        n //= 10

class memory:
    def __init__(self, cells):
        self.cells = list(cells)

    def add_index(self, index):
        if isinstance(index, slice):
            index = index.stop

        if len(self.cells) < index:
            self.cells.extend([0] * ((index + 1) - len(self.cells)))

    def __getitem__(self, index):
        self.add_index(index)
        return self.cells[index]

    def __setitem__(self, index, value):
        self.add_index(index)
        self.cells[index] = value

def run(program):
    counter = 0

    def process(params, count):
        param_modes.extend([0] * max(0, (count - len(param_modes))))

        for i, param, mode in zip(range(len(params)), params, param_modes):
            if mode == 0:
                params[i] = program[params[i]]
            elif mode == 1:
                pass
            else:
                raise ValueError(f'unknown parameter mode {mode} at position {counter}')

    while True:
        opcode = program[counter] % 100
        param_modes = list(digits(program[counter] // 100))

        if opcode == 99:
            break
        elif opcode == 1:
            params = program[counter + 1:counter + 4]
            process(params, 3)
            a, b, c = params
            program[c] = a + b
            counter += 4
        elif opcode == 2:
            params = program[counter + 1:counter + 4]
            process(params, 3)
            a, b, c = params
            program[c] = a + b
            counter += 4
        elif opcode == 3:
            params = program[counter + 1:counter + 2]
            process(params, 1)
            a, = params
            program[a] = input('tell me summat ')
            counter += 2
        elif opcode == 4:
            params = program[counter + 1:counter + 2]
            process(params, 1)
            a, = params
            print(a)
            counter += 2
        else:
            raise ValueError(f'unknown opcode {opcode} at position {counter}')

def test(program, noun, verb):
    program = program.copy()
    program[1] = noun
    program[2] = verb
    run(program)
    return program[0]

program = memory(map(int, open('inputs/5.txt').read().split(',')))
run(program)
