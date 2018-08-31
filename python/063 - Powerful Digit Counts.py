import time

start = time.time()

count = 0

for num in range(1,100000):
	for power in range(1,100):
		if power == len(str(num**power)):
			count += 1
	print(num)

print(count)

end = time.time()

print(end-start)