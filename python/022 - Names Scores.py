letters = {}
let_num = 1
name_count = 1
total = 0

for let in 'abcdefghijklmnopqrstuvwxyz':
	letters[let] = let_num
	let_num += 1

with open('.\\figures\\022.txt','r') as f:
	for mess in f:
		names = mess.replace('\"','').split(',')
		names_sorted = sorted(names, key=str.lower)
		for name in names_sorted:
			name_score = 0
			name_total = 0
			for letter in name:
				letter_score = letters.get(letter.lower(),0)
				name_score += letter_score
			name_total = name_score * name_count
			total += name_total
			#print(name,name_count,name_score,name_total,total)
			name_count += 1


print(total)