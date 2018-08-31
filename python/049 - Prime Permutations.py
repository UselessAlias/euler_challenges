import itertools as it
from Euler_Functions import prime_eratosthenes

primes = prime_eratosthenes(10000)
iter_primes_lists = []
primes_tested = set()

for prime in primes:
	if prime < 1000:
		continue
	iter_primes = set()
	for iteration in it.permutations(str(prime)):
		clean_iter = ''.join(iteration)
		if int(clean_iter) in primes and len(str(int(clean_iter))) == 4:
			iter_primes.add(int(clean_iter))
	if len(primes_tested & iter_primes) == 0 and len(iter_primes) > 2:
		iter_primes_lists.append(iter_primes)
	primes_tested.add(prime)

for primes_list in iter_primes_lists:
	combs = list(it.combinations(primes_list,3))
	for comb in combs:
		diff_1 = comb[1] - comb[2]
		diff_2 = comb[0] - comb[1]
		if abs(diff_1) == abs(diff_2):
			print(str(comb[0]) + str(comb[1]) + str(comb[2]))