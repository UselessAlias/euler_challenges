import math

def prime_eratosthenes(n):
    not_prime_list = []
    prime_list = []
    for i in range(2, n+1):
        if i not in not_prime_list:
            #print (i)
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                not_prime_list.append(j)
    return prime_list

num = 600851475143
lpf = []
primes = prime_eratosthenes(100000)

for prime in primes:
	if num % prime == 0:
		lpf.append(prime)
		num = num / prime

print(lpf)