from utils import file2list

def fuel(mass):
    return mass // 3 - 2

print(sum(map(fuel, file2list('inputs/1.txt'))))