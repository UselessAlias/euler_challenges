dis_powers = set()

for a in range (2,101):
	for b in range (2, 101):
		num = a ** b
		dis_powers.add(num)

print(len(dis_powers))