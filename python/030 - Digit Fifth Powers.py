power = 5
max_num = (9**power) * power
num = 10
ans = 0

while num <= max_num:
	str_num = str(num)
	pow_sum_num = 0
	for dig in str_num:
		pow_sum_num += int(dig)**power
	if pow_sum_num == num:
		ans += num
	num += 1

print(ans)