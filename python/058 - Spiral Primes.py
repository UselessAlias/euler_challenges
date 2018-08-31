from Euler_Functions import spiral_diagonal_grid, prime_eratosthenes

primes = prime_eratosthenes(10000000)
prime_list = sorted(list(primes))
length = 7

perc = 100

#while perc > 10:
#	prime_count = 0
#	non_prime_count = 0
#	spiral = spiral_diagonal_grid(length)
#	for y in spiral:
#		for num in y:
#			if num == 0:
#				continue
#			if num in primes:
#				prime_count += 1
#			else:
#				non_prime_count += 1
#	perc = (prime_count*100)/(non_prime_count + prime_count)
#	print(length, perc, prime_count, non_prime_count)
#	length += 2
#
#print(length-2)

length = 1
num_ne = 1
prime_count = 0
non_prime_count = 0

while perc > 10:
	length += 2
	add = length - 1
	num_se = num_ne + add
	num_sw = num_se + add
	num_nw = num_sw + add
	num_ne = num_nw + add
	new_nums = [num_nw,num_ne,num_sw,num_se]
	for num in new_nums:
		if num < 10000000:
			if num in primes:
				prime_count += 1
			else:
				non_prime_count += 1
		else:
			sqrt = ((num ** 0.5) + 1) // 1
			if num % 2 == 0:
				non_prime_count += 1
			else:
				for div in prime_list:
					if div > int(num ** 0.5):
						prime_count += 1
						break
					elif num % div == 0:
						non_prime_count += 1
						break

	perc = (prime_count*100)/(non_prime_count + prime_count+1)
	print(length, perc, num_se,num_sw,num_nw,num_ne,prime_count,non_prime_count)

print(length)