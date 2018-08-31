import Euler_Functions
import operator

primes = Euler_Functions.prime_eratosthenes(10000000)
quads = {}

for b in primes:
	if b >= 1000:
		continue
	for a in range(-999,1000):
		for n in range(1,1000):
			calc = (n*n) + (a*n) + b
			if calc not in primes:
				quads[(a,b)] = n
				break

result = max(quads.items(), key=operator.itemgetter(1))[0]
print(result)
print(quads[result])
print(result[0] * result[1])