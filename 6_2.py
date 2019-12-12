from collections import defaultdict

data = tuple(line.strip().split(')') for line in open('inputs/6.txt'))
transfer_map = defaultdict(lambda: [])

for orbitee, orbiter in data:
	transfer_map[orbiter].append(orbitee)

for orbitee, orbiter in data:
	transfer_map[orbitee].append(orbiter)

current_objects = [transfer_map['YOU'][0]]
transfer_count = 0
visited_objects = set()

while 'SAN' not in current_objects:
	new_objects = []

	for obj in current_objects:
		visited_objects.add(obj)
		new_objects.extend(new_obj for new_obj in transfer_map[obj] if new_obj not in visited_objects)

	current_objects = new_objects
	transfer_count += 1

print(transfer_count - 1)