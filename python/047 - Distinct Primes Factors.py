from Euler_Functions import Prime_Factors, prime_eratosthenes

quad_counter = 0
seed = 2
primes = prime_eratosthenes(200000)

while quad_counter < 4:
	length = len(Prime_Factors(seed, unique=True, prime_list=primes))
	if length == 4:
		quad_counter += 1
		seed -= 1
		continue
	else:
		quad_counter = 0
		seed += 4
		
print(seed+1)