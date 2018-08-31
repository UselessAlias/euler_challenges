from math import factorial

sumo = 0

for x in range(3,1000000):
	x_str = str(x)
	x_str_sum = 0
	for dig in x_str:
		x_str_sum += factorial(int(dig))
	if x == x_str_sum:
		sumo += x

print(sumo)