from Euler_Functions import prime_eratosthenes

primes = prime_eratosthenes(1000000)
primes_ordered = sorted(list(primes))
con_prime_sum = []

for seed_prime in primes_ordered:
	seed_index = primes_ordered.index(seed_prime)
	count = 1
	sumo = seed_prime
	add_index = 1
	while sumo < 1000000:
		try:
			sumo += primes_ordered[seed_index+add_index]
		except:
			break
		count += 1
		if sumo in primes:
			con_prime_sum.append((sumo,count))
		add_index += 1
	print(seed_prime)

print(sorted(con_prime_sum, key=lambda x: x[1]))