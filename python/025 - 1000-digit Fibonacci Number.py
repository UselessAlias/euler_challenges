fib_current = 0
fib1 = 1
fib2 = 1
fib_count = 2

while len(str(fib_current)) < 1000:
	fib_current = fib1 + fib2
	fib1 = fib2
	fib2 = fib_current
	fib_count += 1

print(fib_count)
