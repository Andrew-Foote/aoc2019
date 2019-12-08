from collections import defaultdict

data = tuple(line.strip().split(')') for line in open('inputs/6.txt'))
direct_orbitee_map = {orbiter: orbitee for orbitee, orbiter in data}

s = 0

for orbitee, orbiter in data:
	s += 1

	while orbitee != 'COM':
		s += 1
		orbitee = direct_orbitee_map[orbitee]

print(s)