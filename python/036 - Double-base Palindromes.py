from Euler_Functions import Is_Palindrome

pal_nums = []
sumo = 0

for num in range(1,1000001):
	bin_num = str(bin(num))[2:]
	num_str = str(num)
	if Is_Palindrome(bin_num) and Is_Palindrome(num_str):
		pal_nums.append((num,bin_num))
		sumo += num

print(sumo)