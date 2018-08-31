from Euler_Functions import prime_eratosthenes

primes = prime_eratosthenes(1000000)

truncs = []
sumo = 0

for prime in primes:
	if len(str(prime)) == 1:
		continue
	prime_str = str(prime)
	splice_prime_l = prime_str[1:]
	splice_prime_r = prime_str[:len(prime_str)-1]
	while len(splice_prime_l) > 0:
		if int(splice_prime_l) not in primes or int(splice_prime_r) not in primes:
			break
		splice_prime_l = splice_prime_l[1:]
		splice_prime_r = splice_prime_r[:len(splice_prime_r)-1]
	if len(splice_prime_l) == 0:
		truncs.append(prime)
		sumo += prime
		print('One more prime')

print(truncs)
print(sumo)