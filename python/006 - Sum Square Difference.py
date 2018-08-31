sum_squares = 0
squared_sum = 0
for num in range(1,101):
	sum_squares += num**2
	squared_sum += num
print((squared_sum**2)-sum_squares)