with open(r'.\figures\059.txt', 'r') as f:
	for row in f:
		data = row

row = row.split(',')
combs = [(i,j,k) for i in range(0,128) for j in range(0,128) for k in range(0,128)]

same_crypt_1 = []
same_crypt_2 = []
same_crypt_3 = []

bit = []

for let in row:
	bit.append(int(let))
	if len(bit) == 3:
		same_crypt_1.append(bit[0])
		same_crypt_2.append(bit[1])
		same_crypt_3.append(bit[2])
		bit = []

if len(bit) == 1:
	same_crypt_1.append(bit[0])

if len(bit) == 2:
	same_crypt_1.append(bit[0])
	same_crypt_2.append(bit[1])

count_crypt_1 = {}
for let in same_crypt_1:
	count_crypt_1[let] = count_crypt_1.get(let, 0) + 1
sort_crypt_1 = sorted(count_crypt_1.items(), key= lambda x:x[1], reverse=True)
count_crypt_2 = {}
for let in same_crypt_2:
	count_crypt_2[let] = count_crypt_2.get(let, 0) + 1
sort_crypt_2 = sorted(count_crypt_2.items(), key= lambda x:x[1], reverse=True)
count_crypt_3 = {}
for let in same_crypt_3:
	count_crypt_3[let] = count_crypt_3.get(let, 0) + 1
sort_crypt_3 = sorted(count_crypt_3.items(), key= lambda x:x[1], reverse=True)

r = [num for num in range(32,127)]

def valid_key(key,string):
	for let in string:
		de = let ^ key
		if de not in r:
			return False
	return True

poss_keys_1 = []
poss_keys_2 = []
poss_keys_3 = []

for key in range(97,123):
	if valid_key(key, same_crypt_1):
		poss_keys_1.append(key)
	if valid_key(key, same_crypt_2):
		poss_keys_2.append(key)
	if valid_key(key, same_crypt_3):
		poss_keys_3.append(key)

combs = [(a,b,c) for a in poss_keys_1 for b in poss_keys_2 for c in poss_keys_3]

for comb in combs:
	sumo = 0
	word_1 = ''
	for let in same_crypt_1:
		sumo += let ^ comb[0]
		word_1 += chr(let ^ comb[0])
	word_2 = ''
	for let in same_crypt_2:
		sumo += let ^ comb[1]
		word_2 += chr(let ^ comb[1])
	word_3 = ''
	for let in same_crypt_3:
		sumo += let ^ comb[2]
		word_3 += chr(let ^ comb[2])
	index = 0
	text = ''
	while 1==1:
		try:
			text += word_1[index]
		except:
			break
		try:
			text += word_2[index]
		except:
			break
		try:
			text += word_3[index]
		except:
			break
		index += 1
	count_let_1 = {}
	count_let_2 = {}
	count_let_3 = {}
	text = list(text)
	for let in word_1:
		count_let_1[let] = count_let_1.get(let,0) + 1
	for let in word_2:
		count_let_2[let] = count_let_2.get(let,0) + 1
	for let in word_3:
		count_let_3[let] = count_let_3.get(let,0) + 1
	count_let_sort_1 = sorted(count_let_1.items(), key= lambda x: x[1], reverse=True)
	count_let_sort_2 = sorted(count_let_2.items(), key= lambda x: x[1], reverse=True)
	count_let_sort_3 = sorted(count_let_3.items(), key= lambda x: x[1], reverse=True)
	if count_let_sort_1[0][0] == ' ' and count_let_sort_2[0][0] == ' ' and count_let_sort_3[0][0] == ' ':
		print(''.join(text))
		print(sumo)
		break