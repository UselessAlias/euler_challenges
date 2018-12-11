import time

start = time.time()

for num in range(20, 1000000000,20):
	done = False
	for div in range(2, 21):
		if num % div != 0:
			break
		if div == 20:
			done = True
	if done:
		break

print(num)

end = time.time()

print(end - start)
