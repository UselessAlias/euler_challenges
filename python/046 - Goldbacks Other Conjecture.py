from Euler_Functions import prime_eratosthenes

primes = prime_eratosthenes(10000)
twice_squares = [2*i*i for i in range(1,10000)]
odds = [i for i in range(1,10000,2)]

primes_set = set(primes)
twice_squares_set = set(twice_squares)
odd_composite_set = set(odds) - primes_set

for prime in primes_set:
	for num in twice_squares_set:
		test = prime + num
		odd_composite_set.discard(test)

print(odd_composite_set)