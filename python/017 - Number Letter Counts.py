from num2words import num2words
letters = 0

for num in range(1,1001):
	str = num2words(num).replace('-', ' ').split()
	for words in str:
		letters += len(words)

print(letters)