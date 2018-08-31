import itertools

perms = itertools.permutations('0123456789')
perms_tuples = list(perms)
perms_list = []

for tup in perms_tuples:
	perms_list.append(int(''.join(tup)))

perm_sort = sorted(perms_list)

print(perm_sort[999999])