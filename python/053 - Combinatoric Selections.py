from math import factorial

over_mil_count = 0

for n in range(1,101):
 	for r in range(0,n+1):
 		if r == 0 or r == n:
 			comb = 1 
 		else:
	 		comb = factorial(n)/(factorial(r)*factorial(n-r))
	 	if comb > 1000000:
	 		over_mil_count += 1

print(over_mil_count)