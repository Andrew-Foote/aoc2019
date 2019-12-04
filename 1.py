from utils import file2list

def fuel(mass):
    return mass // 3 - 2

print(sum(fuel(int(mass)) for mass in open('inputs/1.txt')))