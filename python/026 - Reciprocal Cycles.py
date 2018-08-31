import decimal
from fractions import Fraction

decimal.getcontext().prec = 10000

rep_len = {}

for div in range(3,1000):
	dec = decimal.Decimal(1)/decimal.Decimal(div)
	decimals = str(dec)[2:]
	#print(div)
	#print(dec)
	for length in range(1,len(decimals)):
		rep = decimals[:length]
		start_count = 0
		#print(rep)
		try:
			for start_pos in range(0,len(decimals)-length,length):
				ques_rep = decimals[start_pos+length:start_pos+length+length]
				#print(ques_rep)
				#print(start_pos)
				if rep != ques_rep:
					#print('break')
					break
				elif rep == ques_rep and start_count == 8:
					rep_len[div] = length
					#print('added')
					raise Exception('Please Work')
				start_count += 1
		
		except Exception as stop:
			#print('Exception')
			break
		#print('broken')

#print(rep_len)
print(max(rep_len, key=lambda i: rep_len[i]))