sumo = 1
adds = 0

for num in range(1,101):
	sumo *= num

txt = str(sumo)

for dig in txt:
	adds += int(dig)

print(adds)
