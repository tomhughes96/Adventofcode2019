def passcounter():
	k = 0
	j = 0
	c = 0
	for i in range(254032,789861):
		i = str(i)
		if int(i[1]) >= int(i[0]) and int(i[2]) >= int(i[1]) and int(i[3]) >= int(i[2]) and int(i[4]) >= int(i[3]) and int(i[5]) >= int(i[4]):
			if i[1] == i[0] or i[2] == i[1] or i[3] == i[2] or i[4] == i[3] or i[5] == i[4]:
				k +=  1
				if i[0] == i[1] and c == 0:
					if i[1] != i[2]:
						j += 1
						c = 1
				if i[1] == i[2] and c == 0:
					if i[2] != i[3] and i[0] != i[1]:
						j += 1
						c = 1
				if i[2] == i[3] and c == 0:
					if i[3] != i[4] and i[1] != i[2]:
						j += 1
						c = 1
				if i[3] == i[4] and c == 0:
					if i[4] != i[5] and i[2] != i[3]:
						j += 1
						c = 1
				if i[4] == i[5] and c == 0:
					if i[3] != i[4]:
						j += 1
		c = 0

				#if i[0] == i[1] and i[1] == i[2] or i[1] == i[2] and i[2] == i[3] or i[2] == i[3] and i[3] == i[4] or i[3] == i[4] and i[4] == i[5]:
				#	j = j + 1 part 1
	print(j)

passcounter()

#answers
#1033
#670
