seed = 1

tri_set = set()
pent_set = set()
hex_set = set()

while seed <= 100000:
	tri_num = seed*(seed + 1)/2
	pent_num = seed*(3*seed - 1)/2
	hex_num = seed*(2*seed - 1)
	tri_set.add(tri_num)
	pent_set.add(pent_num)
	hex_set.add(hex_num)
	seed += 1

combo_set = tri_set & pent_set & hex_set

print(combo_set)