import numpy as np
import random

def prime_eratosthenes(n):
    not_prime_list = set()
    prime_counter = 1
    prime_list = set()
    
    for i in range(2,n):
        if i not in not_prime_list \
        and prime_counter < n + 1:
            prime_list.add(i)
            prime_counter += 1
            for j in range(i*i, n+1, i):
                not_prime_list.add(j)
        elif prime_counter == n + 1:
        	break
        else:
        	pass

    return prime_list

def is_prime(n, k = 3):
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n % 2 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d % 2 == 0:
         s, d = s + 1, d >> 1
      # A for loop with a random sample of numbers
      for a in random.sample(range(2, n-2), k):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True

def spiral_diagonal_grid(length):
    grid = np.zeros((length,length), dtype=int)
    size = grid.size
    start_pos_x = int((grid.shape[0] + 1) / 2) - 1
    start_pos_y = int((grid.shape[1] + 1) / 2) - 1
    num = 1
    pos_x_s = start_pos_x
    pos_x_n = start_pos_x
    pos_y_w = start_pos_y
    pos_y_e = start_pos_y
    pos_shift = 2

    grid[start_pos_x, start_pos_y] = 1
    while num < size:
        pos_x_s += 1
        pos_x_n -= 1
        pos_y_w -= 1
        pos_y_e += 1
        num += pos_shift
        grid[pos_x_s,pos_y_e] = num
        num += pos_shift
        grid[pos_x_s,pos_y_w] = num
        num += pos_shift
        grid[pos_x_n,pos_y_w] = num
        num += pos_shift
        grid[pos_x_n,pos_y_e] = num
        pos_shift += 2

    return grid

def simplified_fraction(numerator,denominator):
    while div <= numerator:
        if numerator % div == 0 and denominator % div == 0:
            numerator /= div
            denominator /= div
        else:
            div += 1

    return(numerator,denominator)

def Is_Palindrome(string):
    forward = string
    backward = string[::-1]
    if forward == backward:
        return(True)
    else:
        return(False)

def Is_Pandigital(num, with_zero=False):
    start_value = 1
    if with_zero:
        start_value = 0
    num_str = str(num)
    nums_set = set([str(i) for i in range(start_value,len(num_str)+1)])
    num_str_set = set(list(num_str))
    if len(num_str_set) != len(num_str):
        return False
    if nums_set >= num_str_set:
        return True

def Prime_Factors(num, unique=False, factorised=True, prime_list=None):
    if unique:
        prime_factors = set()
    else:    
        prime_factors = []  
    if prime_list == None:
        primes = prime_eratosthenes(num+1)
    else:
        primes = prime_list
    #un-indexed
    if factorised:
        for prime in primes:
            while num % prime == 0:
                num /= prime
                if unique:
                    prime_factors.add(prime)
                else:
                    prime_factors.append(prime)
    else:
        #indicies
        for prime in primes:
            factor = 1
            while num % prime == 0:
                factor *= prime
                num /= prime
            if factor > 1:
                if unique:
                    prime_factors.add(factor)
                else:
                    prime_factors.append(factor)
        
    return prime_factors

def num_counter(number):
    num_count = [0,0,0,0,0,0,0,0,0,0]
    for dig in str(number):
        num_count[int(dig)] += 1
    return num_count