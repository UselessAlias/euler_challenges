lengths = []
starter = 2

while starter < 1000000:
	counter = 1
	collatz = starter
	#print(collatz)
	x = 0
	while collatz != 1 and x == 0:
		if collatz % 2 == 0:
			collatz = collatz/2
			#print(collatz)
			if collatz == 1:
				counter += 1
				lengths.append(counter)
				x = 1
			else:
				counter += 1
		elif collatz % 2 == 1:
			collatz = 3*collatz + 1 
			if collatz == 1:
				counter += 1
				lengths.append(counter)
				x = 1
			else:
				counter += 1
	starter += 1

pos = max(lengths)
ans = lengths.index(pos) + 2
print(ans)