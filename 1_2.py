from utils import file2list

def fuel(mass):
    # mass // 3 - 2 <= 0 iff mass // 3 <= 2, i.e. mass <= 8
    if mass <= 8:
        return 0

    fuel_ = mass // 3 - 2
    return fuel_ + fuel(fuel_)

print(sum(map(fuel, file2list('inputs/1.txt'))))