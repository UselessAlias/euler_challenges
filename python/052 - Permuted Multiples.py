import itertools as it

for i in it.count(1):
	set_i = set(list(str(i)))
	for j in range(1,7):
		set_j = set(list(str(i*j)))
		diff_set = set_i | set_j
		if len(diff_set) != len(set_i):
			j = 0
			break
	if j == 6:
		print(i)
		break