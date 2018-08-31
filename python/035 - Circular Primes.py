import itertools
from Euler_Functions import prime_eratosthenes

mil_primes = prime_eratosthenes(1000000)
circ_primes = [2,5]
count = 2
cycle_count = 1

for prime in mil_primes:
	prime_str = str(prime)
	if any(num in prime_str for num in ['0','2','4','5','6','8']):
		continue
	cycle = [prime_str]
	cycle_count += 1
	prime_str_new = prime_str[1:len(prime_str)] + prime_str[0] 
	while prime_str_new != prime_str:
		cycle.append(prime_str_new)
		prime_str_new = prime_str_new[1:len(prime_str)] + prime_str_new[0]
	if any(int(cyc) not in mil_primes for cyc in cycle):
		continue
	circ_primes.append(prime)
	count += 1

print(count)
