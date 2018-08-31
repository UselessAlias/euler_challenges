pan_nums = []

for num in range(1,10000):
	num_set = set([str(i) for i in range(1,10)])
	num_str = str(num)
	mult = 2
	while len(num_str) < 9:
		num_str += str(num*mult)
		mult += 1
	if len(num_str) > 9:
		continue
	num_str_set = set(list(num_str))
	comb_set = num_set - num_str_set
	if len(comb_set) == 0:
		pan_nums.append(int(num_str))

print(sorted(pan_nums, reverse=True))