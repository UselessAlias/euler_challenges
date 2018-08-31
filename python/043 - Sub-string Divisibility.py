from itertools import permutations

sumo = 0

for n in permutations('0123456789'):
	num = ''.join(n)
	if num[0] == '0':
		continue
	if int(num[1]+num[2]+num[3]) % 2 != 0:
		continue
	if int(num[2]+num[3]+num[4]) % 3 != 0:
		continue
	if int(num[3]+num[4]+num[5]) % 5 != 0:
		continue
	if int(num[4]+num[5]+num[6]) % 7 != 0:
		continue
	if int(num[5]+num[6]+num[7]) % 11 != 0:
		continue
	if int(num[6]+num[7]+num[8]) % 13 != 0:
		continue
	if int(num[7]+num[8]+num[9]) % 17 != 0:
		continue
	sumo += int(num)

print(sumo)