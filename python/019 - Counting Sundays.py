date = [1900,1,1,1]
thirty_days = [4,6,9,11]
normal_days = [1,3,5,7,8,10,12]
sundays = 0

while date[0] < 2001:
	if date[3] == 7 and date[0] > 1900 and date[0] < 2001 and date[2] == 1:
		sundays += 1
	
	if date[3] == 7:
		date[3] = 1
	else:
		date[3] += 1

	if date[1] in thirty_days and date[2] == 30:
		date[2] = 1
		date[1] += 1
	elif date[1] in normal_days and date[2] == 31:
		date[2] = 1
		date[1] += 1
	elif date[1] == 2 and date[2] == 28 and date[0] % 400 == 0:
		date[2] += 1
	elif date[1] == 2 and date[2] == 28 and date[0] % 100 == 0:
		date[2] = 1
		date[1] += 1
	elif date[1] == 2 and date[2] == 28 and date[0] % 4 != 0:
		date[2] = 1
		date[1] += 1
	elif date[1] == 2 and date[2] == 29:
		date[2] = 1
		date[1] += 1
	else:
		date[2] += 1

	if date[1] == 13:
		date[1] = 1
		date[0] += 1

print(sundays)