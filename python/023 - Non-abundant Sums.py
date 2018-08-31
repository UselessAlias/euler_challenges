import math
import numpy as np

divisors = {}
abundant = []
abundant_sums = []
ans = 0

for num in range(2,28123):
	sqrt = math.sqrt(num)
	ceil = math.ceil(sqrt)
	div_sum = 1
	for div in range(2,ceil):
		if num % div == 0:
			dived = num / div
			div_sum += dived + div
	if num % sqrt == 0 :
		div_sum += sqrt
	divisors[num] = div_sum

for num in divisors:
	if num < divisors[num]:
		abundant.append(num)

np_abundant = np.array(abundant)
nums = range(28123)
np_nums = np.array(nums)

for num1 in abundant:
	index = abundant.index(num1)
	for num2 in abundant[index:]:
		add = num1 + num2	
		if add >= 28123:
			break
		else:
			abundant_sums.append(add)

abundant_set = set(abundant_sums)
nums_set = set(nums)

to_sum = nums_set.difference(abundant_set)
print(to_sum)
print(sum(to_sum))