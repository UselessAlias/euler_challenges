seed = 1
min_diff = 10000000000
pent_nums = set()

while seed <= 10000:
	pent_num = seed*(3*seed - 1)/2
	pent_nums.add(pent_num)
	seed += 1

for a in pent_nums:
	for b in pent_nums:
		if a <= b:
			continue
		add = a + b
		diff = a - b
		if add in pent_nums:
			if diff in pent_nums:
				if min_diff > diff:
					min_diff = diff

print(min_diff)