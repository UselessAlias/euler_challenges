from Euler_Functions import prime_eratosthenes, is_prime
from itertools import combinations
import time

start = time.time()

n = 10000
m = 2700000
primes = prime_eratosthenes(m)
primes_set_list = sorted(list(prime_eratosthenes(n)))
seeds = [i for i in primes_set_list if i < 1000]

def comb_primes_test(prime_list, new_prime):
	for tested_prime in prime_list:
		pre = int(str(new_prime) + str(tested_prime))
		if pre < m:
			if pre not in primes:
				return False
		else:
			sqrt = ((pre ** 0.5) + 1) // 1
			if pre % 2 == 0:
				return False
			else:
				for div in primes_set_list:
					if div > int(pre ** 0.5):
						break
					elif pre % div == 0:
						return False
		post = int(str(tested_prime) + str(new_prime))
		if post < m:
			if post not in primes:
				return False
		else:
			sqrt = ((post ** 0.5) + 1) // 1
			if post % 2 == 0:
				return False
			else:
				for div in primes_set_list:
					if div > int(post ** 0.5):
						break
					elif post % div == 0:
						return False
	return True

print('Made Primes')

def GiveMeResults():
	answers = []
	for a in seeds:
		print(a)
		for b in primes_set_list:
			prime_list = [a]
			if b <= a:
				continue
			if comb_primes_test(prime_list,b):
				for c in primes_set_list:
					prime_list = [a,b]
					if c <= b:
						continue
					if comb_primes_test(prime_list,c):
						for d in primes_set_list:
							prime_list = [a,b,c]
							if d <= c:
								continue
							if comb_primes_test(prime_list,d):
								for e in primes_set_list:
									prime_list = [a,b,c,d]
									if e <= d:
										continue
									if comb_primes_test(prime_list,e):
										prime_list = [a,b,c,d,e]
										print('YES!')
										print(prime_list)
										answer = sum(prime_list)
										answers.append(answer)
	return min(answers)

print(GiveMeResults())

end = time.time()

print(end-start)