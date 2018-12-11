import math
import time

start = time.time()

tri_nums = []
running_tri_num = 0
num = 1

while num > 0:
	running_tri_num += num
	div = 1
	divs = set()
	while div < math.sqrt(running_tri_num):
		if running_tri_num % div == 0:
			divs.add(div)
			divs.add(running_tri_num/div)
		div += 1
	num += 1
	if len(divs) > 500:
		break

print(running_tri_num)

end = time.time()

print((end - start)*1000)