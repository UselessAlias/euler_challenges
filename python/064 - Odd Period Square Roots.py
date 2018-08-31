import math
import time

start = time.time()

counter = 0

for num in range(2,10001):
	if math.sqrt(num) % 1 == 0:
		continue
	else:	
		m_0 = 0
		d_0 = 1
		a_0 = math.floor(math.sqrt(num))

		m_n = m_0
		d_n = d_0
		a_n = a_0

		rep = []

		while True:
			m_n1 = (d_n*a_n) - m_n
			d_n1 = (num - m_n1**2)/d_n
			a_n1 = math.floor((a_0 + m_n1)/d_n1)
			m_n = m_n1
			d_n = d_n1
			a_n = a_n1
			state = (m_n, d_n, a_n)
			if len(rep) == 0:
				rep.append(state)
			else:
				if state == rep[0]:
					repeater = []
					for pos in rep:
						repeater.append(pos[2])
					if len(repeater) % 2 == 1:
						counter += 1
					break
				else:
					rep.append(state)

print(counter)

end = time.time()

print(end-start)