from Euler_Functions import prime_eratosthenes

primes = prime_eratosthenes(10000000)
pan_primes = []

for prime in primes:
	prime_str = str(prime)
	num_set = set([str(i) for i in range(1,len(prime_str)+1)])
	prime_str_set = set(list(prime_str))
	if len(prime_str_set) != len(prime_str):
		continue
	comb_set = num_set - prime_str_set
	if len(comb_set) == 0:
		pan_primes.append(prime)

print(max(pan_primes))