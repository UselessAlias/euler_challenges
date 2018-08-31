numerator = 1
denominator = 1

for y in range(10,100):
	for x in range(10,100):
		if x >= y:
			break
		x_str = str(x)
		y_str = str(y)
		for i in x_str:
			if i == '0':
				continue
			elif x % 11 == 0 or y % 11 == 0:
				continue
			elif i in y_str:
				y_divs = y_str.replace(i,'')
				x_divs = x_str.replace(i,'')
				if x_divs == '0' or y_divs == '0':
					continue
				elif x/y == int(x_divs)/int(y_divs):
					numerator *= x
					denominator *= y

print(numerator,denominator)

div = 2

while div <= numerator:
	if numerator % div == 0 and denominator % div == 0:
		numerator /= div
		denominator /= div
		div = 2
	else:
		div += 1

print(numerator,denominator)