import numpy as np
coins = [2,5,10,20,50,100,200]
amounts = np.ones(201, np.int32)
for coin in coins:
	index = 0
	while index <= 200:
		current_count = amounts[index]
		try:
			amounts[index+coin] += current_count
		except:
			pass
		index += 1
print(amounts)