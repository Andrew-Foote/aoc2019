import sys

def run(program):
    counter = 0

    while True:
        opcode = program[counter]

        if opcode == 99:
            break
        elif opcode == 1:
            a, b, c = program[counter + 1:counter + 4]
            program[c] = program[a] + program[b]
        elif opcode == 2:
            a, b, c = program[counter + 1:counter + 4]
            program[c] = program[a] * program[b]
        else:
            raise ValueError(f'unknown opcode {opcode} at position {counter}')

        counter += 4

def test(program, noun, verb):
    program = program.copy()
    program[1] = noun
    program[2] = verb
    run(program)
    return program[0]

with open('inputs/2.txt') as f:
    program = list(map(int, f.read().split(',')))

for noun in range(100):
    for verb in range(100):
        if test(program, noun, verb) == 19690720:
            print(100 * noun + verb)
            sys.exit()