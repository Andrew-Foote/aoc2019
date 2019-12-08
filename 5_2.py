from dataclasses import dataclass
import typing as t

def digits(n):
    while n > 0:
        yield n % 10
        n //= 10

class Memory:
    def __init__(self, cells):
        self.cells = list(cells)

    def add_index(self, index):
        if isinstance(index, slice):
            index = index.stop

        if index < len(self.cells):
            return

        if len(self.cells) < index:
            self.cells.extend([0] * ((index + 1) - len(self.cells)))

    def __getitem__(self, index):
        self.add_index(index)
        return self.cells[index]

    def __setitem__(self, index, value):
        self.add_index(index)
        self.cells[index] = value

@dataclass
class Op:
    callable_: t.Callable

    # True = input parameter
    # False = output parameter
    params: t.List[bool]

class ProgramMemory(Memory):
    def __init__(self, cells, counter=0):
        super().__init__(cells)
        self.counter = counter

    def offset2index(self, offset):
        if isinstance(offset, slice):
            new_start = None if offset.start is None else offset.start + self.counter
            new_stop = None if offset.stop is None else offset.stop + self.counter

            return slice(new_start, new_stop, offset.step)
        else:
            return offset + self.counter

    def get_offset(self, offset):
        return self[self.offset2index(offset)]

    def set_offset(self, offset, value):
        self[self.offset2index(offset)] = value

    def halt(self):
        self.counter = -1

    def add(self, a, b, c):
        self[c] = a + b

    def multiply(self, a, b, c):
        self[c] = a * b

    def read(self, a):
        self[a] = int(input('> '))

    def write(self, a):
        print(a)

    def jump_true(self, a, b):
        if a:
            self.counter = b
            return True

    def jump_false(self, a, b):
        if not a:
            self.counter = b
            return True

    def less_than(self, a, b, c):
        self[c] = int(a < b)

    def equals(self, a, b, c):
        self[c] = int(a == b)

    def step(self):
        modes, op = divmod(self.get_offset(0), 100)
        op = self.OPCODE_MAP[op]
        modes = list(digits(modes))
        mode_count = len(modes)
        param_count = len(op.params)

        if mode_count < param_count:
            modes.extend([0] * (param_count - mode_count))

        self.counter += 1
        params = self.get_offset(slice(0, param_count))

        for i, param, is_input_param, mode in zip(range(param_count), params, op.params, modes):
            if is_input_param and mode == 0:
                params[i] = self[params[i]]          

        counter_modified = op.callable_(self, *params)

        if not counter_modified:
            self.counter += param_count

    def run(self):
        while self.counter >= 0:
            self.step()

HALT = Op(ProgramMemory.halt, [])
ADD = Op(ProgramMemory.add, [True, True, False])
MULTIPLY = Op(ProgramMemory.multiply, [True, True, False])
READ = Op(ProgramMemory.read, [False])
WRITE = Op(ProgramMemory.write, [True])
JUMP_TRUE = Op(ProgramMemory.jump_true, [True, True])
JUMP_FALSE = Op(ProgramMemory.jump_false, [True, True])
LESS_THAN = Op(ProgramMemory.less_than, [True, True, False])
EQUALS = Op(ProgramMemory.equals, [True, True, False])

ProgramMemory.OPCODE_MAP = {
    99: HALT,
    1: ADD,
    2: MULTIPLY,
    3: READ,
    4: WRITE,
    5: JUMP_TRUE,
    6: JUMP_FALSE,
    7: LESS_THAN,
    8: EQUALS,
}

program = ProgramMemory(map(int, open('inputs/5.txt').read().split(',')))
program.run()
