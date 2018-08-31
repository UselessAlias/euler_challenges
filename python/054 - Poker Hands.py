import re

scores = {}
winner_count_1 = {}
winner_count_2 = {}


face_values = {
	'T'	: '10',
	'J' : '11',
	'Q' : '12',
	'K' : '13',
	'A' : '14'
}

def value(card):
	return card[0]

def suit(card):
	return card[1]

def hand_value(hand_card_split):
	card_counts = {}
	suit_set = set()
	values = []

	for card in hand_card_split:
		suit_set.add(suit(card))
		card_counts[value(card)] = card_counts.get(value(card),0) + 1
		values.append(int(value(card)))

	values = sorted(values, reverse=True)
	values_set = set(values)
	sorted_card_counts = sorted(card_counts.items(), key=lambda x:(int(x[1]),int(x[0])), reverse=True)

	#Royal
	royal_set = ['10','11','12','13','14']
	if values == royal_set:
		royal = True
	else:
		royal = False

	#Flush
	if len(suit_set) == 1:
		flush = True
	else:
		flush = False

	#Straight
	for index in range(0,4):
		if values[index] == values[index+1]+1:
			continue
		else:
			index = 0
			break
	if index == 3:
		straight = True
	else:
		straight = False

	#Of a kind
	value_count = [int(i[0]) for i in sorted_card_counts]
	counts = [int(i[1]) for i in sorted_card_counts]
	if counts[0] == 4:
		of_a_kind = 'four'
	elif counts[0] == 3 and counts[1] == 2:
		of_a_kind = 'full house'
	elif counts[0] == 3:
		of_a_kind = 'three'
	elif counts[0] == 2 and counts[1] == 2:
		of_a_kind = 'two pair'
	elif counts[0] == 2:
		of_a_kind = 'one pair'
	else:
		of_a_kind = False

	#Hand Value
	listy = [int(i[0]) for i in sorted_card_counts]
	if royal and flush:
		return (1, 14, 14)
	elif straight and flush:
		return (2, max(values), max(values))
	elif of_a_kind == 'four':
		return (3, listy, max(values))
	elif of_a_kind == 'full house':
		return (4, listy, max(values))
	elif flush:
		return (5, listy, max(values))
	elif straight:
		return (6, max(values), max(values))
	elif of_a_kind == 'three':
		return (7, listy, max(values))
	elif of_a_kind == 'two pair':
		return (8, listy, max(values))
	elif of_a_kind == 'one pair':
		return (9, listy, max(values))
	else:
		return (10, values, max(values))

with open(r'.\figures\054.txt','r') as f:
	for row in f:

		first_half = row[:len(row)//2]
		last_half = row[(len(row)//2):]
		for i,j in face_values.items():
			first_half = first_half.replace(i,j)
			last_half = last_half.replace(i,j)

		hand_list_1 = first_half.split()
		hand_list_2 = last_half.split()
		
		card_split_1 = []
		for card in hand_list_1:
			card_split_1.append((card[:len(card)-1],card[-1]))

		card_split_2 = []
		for card in hand_list_2:
			card_split_2.append((card[:len(card)-1],card[-1]))

		score_1 = hand_value(card_split_1)
		score_2 = hand_value(card_split_2)

		if score_1[0] < score_2[0]:
			scores['Player 1 wins!'] = scores.get('Player 1 wins!', 0) + 1
			winner = 1
		elif score_1[0] > score_2[0]:
			scores['Player 2 wins!'] = scores.get('Player 2 wins!', 0) + 1
			winner = 2
		else:
			if score_1[1] > score_2[1]:

				scores['Player 1 wins!'] = scores.get('Player 1 wins!', 0) + 1
				winner = 1
			elif score_1[1] < score_2[1]:
				scores['Player 2 wins!'] = scores.get('Player 2 wins!', 0) + 1
				winner = 2
			else:
				if score_1[2] > score_2[2]:
					scores['Player 1 wins!'] = scores.get('Player 1 wins!', 0) + 1
					winner = 1
				elif score_1[2] < score_2[2]:
					scores['Player 2 wins!'] = scores.get('Player 2 wins!', 0) + 1
					winner = 2
				else:
					scores['Oh dear!'] = scores.get('Oh dear!', 0) + 1

		if winner == 1:
			hand_score = score_1[0]
			winner_count_1[hand_score] = winner_count_1.get(hand_score,0) + 1
		elif winner == 2:
			hand_score = score_2[0]
			winner_count_2[hand_score] = winner_count_2.get(hand_score,0) + 1

print(scores)