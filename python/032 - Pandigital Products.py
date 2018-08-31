import itertools as it

pos = it.permutations(' 123456789 ')
prods = set()

for perm in pos:
	math = ''.join(perm).split()
	if len(math) != 3:
		continue
	else:
		if int(math[0]) * int(math[1]) == int(math[2]):
			prods.add(int(math[2]))

print(sum(prods))