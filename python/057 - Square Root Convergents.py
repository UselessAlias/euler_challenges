iter_count = 1
count = 0
numerator = 3
denominator = 2

while iter_count < 1000:
	if len(str(numerator)) > len(str(denominator)):
		count += 1
	last_numerator = numerator
	last_denominator = denominator
	numerator = last_numerator + 2*last_denominator
	denominator = last_numerator + last_denominator
	iter_count += 1

print(count)