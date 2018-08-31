sides = 20 
choice_count = [1]
last_choices = [1]

for branches in range(0, sides*2):
	last_choices = choice_count
	choice_count = [1]
	for point in range(0,len(last_choices)):
		try:
			paths = last_choices[point] + last_choices[point + 1]
			choice_count.append(paths)
		except:
			choice_count.append(1)
	#print(choice_count)

print(choice_count[sides])