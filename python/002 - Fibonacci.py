fibonacci = [1,2]
i = 1
j = 2
k = i + j

while k <= 4000000:
	print('section1')
	fibonacci.append(k)
	i = j
	j = k
	k = i + j

print(fibonacci)

total = 0

for i in range(0,len(fibonacci)):
	num = fibonacci[i]
	print(num)
	if num % 2 == 0:
		total += num

print(total)