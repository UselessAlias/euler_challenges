lychrel_count = 0

for num in range(10001):
	num += int(str(num)[::-1])
	iteration = 1
	while str(num) != str(num)[::-1]:
		num += int(str(num)[::-1])
		iteration += 1
		if iteration == 50:
			lychrel_count += 1
			break

print(lychrel_count)