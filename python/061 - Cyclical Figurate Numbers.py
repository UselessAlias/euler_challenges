import time 

start = time.time()

tri_num = 1
square_num = 1
pent_num = 1
hex_num = 1
hept_num = 1
oct_num = 1

tri_nums = set()
square_nums = set()
pent_nums = set()
hex_nums = set()
hept_nums = set()
oct_nums = set()

n = 0

while tri_num < 10000:
	tri_num = (n*(n+1))/2
	if tri_num < 10000 and tri_num > 999:
		tri_nums.add(int(tri_num))
	square_num = n*n
	if square_num < 10000 and square_num > 999:
		square_nums.add(int(square_num))
	pent_num = (n*((3*n)-1))/2
	if pent_num < 10000 and pent_num > 999:
		pent_nums.add(int(pent_num))
	hex_num = n*(2*n - 1)
	if hex_num < 10000 and hex_num > 999:
		hex_nums.add(int(hex_num))
	hept_num = (n*(5*n - 3))/2
	if hept_num < 10000 and hept_num > 999:
		hept_nums.add(int(hept_num))
	oct_num = n*(3*n-2)
	if oct_num < 10000 and oct_num > 999:
		oct_nums.add(int(oct_num))

	n += 1

set_dict = {3:tri_nums,4:square_nums,5:pent_nums,6:hex_nums,7:hept_nums,8:oct_nums}

seeds = [([str(i)[:2],i,str(i)[2:]],[3,4,5,6,7]) for i in oct_nums]

while True:
	seed = seeds.pop()
	builder = seed[0]
	sets = seed[1]
	if len(sets) == 0:
		if builder[0] == builder[2]:
			print(builder[1])
			break
		else:
			continue
	for num in sets:
		test_set = set_dict[num]
		for number in test_set:
			tester = [str(number)[:2],number,str(number)[2:]]
			if builder[2] == tester[0]:
				new_builder = [builder[0],builder[1]+tester[1],tester[2]]
				new_sets = sets.copy()
				new_sets.remove(num)
				new_seed = (new_builder,new_sets)
				seeds.append(new_seed)
			elif builder[0] == tester[2]:
				new_builder = [tester[0],builder[1]+tester[1],builder[2]]
				new_sets = sets.copy()
				new_sets.remove(num)
				new_seed = (new_builder,new_sets)
				seeds.append(new_seed)

def build_test(seed):
	builder = seed[0]
	sets = seed[1]
	if len(sets) == 0:
		if builder[0] == builder[2]:
			return(builder[1])
		else:
			return False
	for num in sets:
		test_set = set_dict[num]
		for number in test_set:
			tester = [str(number)[:2],number,str(number)[2:]]
			if builder[2] == tester[0]:
				new_builder = [builder[0],builder[1]+tester[1],tester[2]]
				new_sets = sets.copy()
				new_sets.remove(num)
				new_seed = (new_builder,new_sets)
				new_result = build_test(new_seed) 
				if new_result != False:
					return new_result
				else:
					pass
			elif builder[0] == tester[2]:
				new_builder = [tester[0],builder[1]+tester[1],builder[2]]
				new_sets = sets.copy()
				new_sets.remove(num)
				new_seed = (new_builder,new_sets)
				new_result = build_test(new_seed)
				if new_result != False:
					return new_result
				else:
					pass
	return(False)

for seed in seeds:
	if build_test(seed) != False:
		print(build_test(seed))

end = time.time()

print(end-start)