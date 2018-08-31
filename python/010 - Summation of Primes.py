def prime_eratosthenes(n):
    not_prime_list = set()
    prime_list = set()
    
    for i in range(2,n+1):
        if i not in not_prime_list:
            prime_list.add(i)
            for j in range(i*i, n+1, i):
                not_prime_list.add(j)

    return prime_list

total = 0
primes = prime_eratosthenes(2000000)

for prime in primes:
    total += prime

print(total)
