from collections import defaultdict
from Euler_Functions import num_counter

cubes = defaultdict(list)

for num in range(1,1000000):
	cube = num**3
	length = len(str(cube))
	cubes[length].append(cube)

def answer():
	for length in cubes.values():
		length_counts = defaultdict(list)
		for number in length:
			length_counts[''.join([str(x) for x in num_counter(number)])].append(number)
		for n in length_counts.values():
			if len(n) > 4:
				return n

print(answer())