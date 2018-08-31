import math

factor_sums = {}
total = 0

for num in range(1,10000):
	sumo = 1
	sqrt = math.sqrt(num)
	ceil = math.ceil(sqrt)
	for div in range(2,ceil):
		if num % div == 0:
			sumo += div
			sumo += (num/div)
	if num % sqrt == 0:
		sumo += sqrt
	factor_sums[num] = sumo

for a in factor_sums:
	b = factor_sums[a]
	if b < 10000 and b != 1:
		c = factor_sums[b]
		if a == c and a != b and a != 1:
			total += a
			
print(total)