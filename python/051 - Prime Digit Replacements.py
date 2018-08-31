from Euler_Functions import prime_eratosthenes
from itertools import combinations

primes = prime_eratosthenes(10000000)
prime_list = sorted(list(primes))

def answer():
	for prime in prime_list:
		length = len(str(prime))
		prime_str = str(prime)
		for comb_length in range(2,length -1):
			try:
				combs = combinations(range(0, length),comb_length)
			except:
				continue
			for comb in combs:
				if len(comb) == 1:
					continue
				prime_family = []
				for num in range(10):	
					index = 0
					prime_build = ''
					while index < length:
						if index in comb:
							prime_build += str(num)
						else:
							prime_build += prime_str[index]
						index += 1
					if prime_build[0] == '0':
						continue
					if int(prime_build) in primes:
						prime_family.append(int(prime_build))
				if len(prime_family) > 7:
					return prime_family

print(answer()[0])