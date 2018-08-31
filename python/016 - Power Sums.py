power = 1

for ind in range(0,1000):
	power *= 2

power_str = str(power)
sumo = 0

for digit in power_str:
	sumo += int(digit)

print(sumo)