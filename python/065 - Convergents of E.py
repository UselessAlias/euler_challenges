terms = [2]
add = 2

while len(terms) < 101:
	terms += [1,add,1]
	add += 2

y = terms.pop()

reverse_terms = terms[::-1][-99:]

z = 1

for x in reverse_terms:
	new_y = x*y + z
	new_z = y
	y = new_y
	z = new_z

numerator = str(y)

sumo = 0

for num in numerator:
	sumo += int(num)

print(sumo)