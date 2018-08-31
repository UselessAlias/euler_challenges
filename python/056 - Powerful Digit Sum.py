max_sum = 0

for a in range(100):
	for b in range(100):
		num = a ** b
		num_str = str(num)
		num_sum = 0
		for digit in num_str:
			num_sum += int(digit)
		if num_sum > max_sum:
			max_sum = num_sum

print(max_sum)