p_count = {}

for p in range(3,1001):
	count = 0
	for c in range(1,p-2):
		for b in range(1,c+1):
			a = p - (c + b)
			if a < 1:
				break
			if a > b:
				continue
			if c*c == (a*a) + (b*b):
				count += 1
	p_count[p] = count
	print(str(p) + ' done')

p_count = sorted(p_count.items(), key=lambda x: x[1])
print(p_count)