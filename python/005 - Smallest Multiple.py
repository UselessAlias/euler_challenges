div_nums = []

for num in range(20, 1000000000,20):
	for div in range(2, 21):
		if num % div != 0:
			break
		elif div == 20:
			div_nums.append(num)
		else:
			pass

print(div_nums)
