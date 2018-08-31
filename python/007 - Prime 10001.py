def prime_eratosthenes(n):
    not_prime_list = set()
    prime_counter = 1
    prime_list = set()
    
    for i in range(2,100000000000):
        if i not in not_prime_list \
        and prime_counter < n + 1:
            prime_list.add(i)
            prime_counter += 1
            for j in range(i*i, 10000000, i):
                not_prime_list.add(j)
        elif prime_counter == n + 1:
        	break
        else:
        	pass

    return max(prime_list)

print(prime_eratosthenes(10001))
