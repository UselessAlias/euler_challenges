pal_nums = []

for num in range(100,1000):
	for mult in range(100,1000):
		x = num * mult
		num_fwd = str(x)
		num_bkwd = num_fwd[::-1]
		if num_fwd == num_bkwd:
			pal_nums.append(x)


print(max(pal_nums))
