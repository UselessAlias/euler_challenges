import math
import time

start = time.time()

answer = 1

for a in range(1,1000):
	for b in range(1,1000 - a):
		pythag = math.sqrt((a*a)+(b*b))
		c = 1000 - a - b
		if pythag == c:
			answer = a * b * c

print(answer)

end = time.time()

print(end - start)