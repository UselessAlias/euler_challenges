import time

start = time.time()

total = 0

for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        
print(total)

end = time.time()

print((end - start)*1000)