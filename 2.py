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

program = list(map(int, open('inputs/2.txt').read().split(',')))
program[1] = 12
program[2] = 2
run(program)
print(program[0])