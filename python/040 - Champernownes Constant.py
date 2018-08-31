dig_count = 0
prod = 1

for num in range(1,1000000):
	num_str = str(num)
	for dig in num_str:
		dig_count += 1
		if dig_count in [1,10,100,1000,10000,100000,1000000]:
			prod *= int(dig)
		if dig_count == 1000000:
			break

print(prod)