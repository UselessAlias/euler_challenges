path = r'.\figures\018.txt'
file = open(path,'r')
route_1 = 0
route_2 = 0
max_row = 16
rows = []
running_sum = [0]

for row in file:
	rows.append(row.split())

for r in rows:
	current_totals = running_sum
	running_sum = []
	index = 0
	for num in r:
		if index == 0:
			tot = int(num) + current_totals[index]
			running_sum.append(tot)
		elif index == len(current_totals) and index != 0:
			tot = int(num) + current_totals[index-1]
			running_sum.append(tot)
		else:
			tot1 = int(num) + current_totals[index-1]
			tot2 = int(num) + current_totals[index]
			if tot1 < tot2:
				running_sum.append(tot2)
			else:
				running_sum.append(tot1)
		index += 1
	print(running_sum)

print(max(running_sum))
