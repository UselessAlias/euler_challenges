with open(r'.\figures\042.txt','r') as f:
	for row in f:
		words = row.replace('"','').split(',')

num_value = {i:j+1 for j,i in enumerate('abcdefghijklmnopqrstuvwxyz')}

triangle_numbers = set()

seed = 1
t_number = 1

while t_number < 200:
	t_number = (seed*(seed+1))/2
	triangle_numbers.add(t_number)
	seed += 1

triangle_word_count = 0

for word in words:
	word_value = 0
	for letter in word:
		word_value += num_value[letter.lower()]
	if word_value in triangle_numbers:
		triangle_word_count += 1

print(triangle_word_count)