def outcode(intcode, inpt, i):
	intcode = list(intcode)
	s = len(intcode)

	while i < s:

		storei = intcode[i]
		enter = str(intcode[i]).zfill(5)
		parameter1 = enter[-3]
		parameter2 = enter[-4]
		parameter3 = enter[-5]
		intcode[i] = int(enter[-2])* 10 + int(enter[-1])

		if parameter1 == '0': #position mode
			if i+1 < s:
				X = intcode[i+1]
		elif parameter1 == '1': #immediate mode
			X = i + 1

		if parameter2 == '0':
			if i+2 < s: 
				Y = intcode[i+2]
		elif parameter2 == '1':
			Y = i + 2

		if parameter3 == '0':
			if i+3 < s: 
				Z = intcode[i+3]
		elif parameter3 == '1':
			Z = i + 3

		if intcode[i] == 1:
			intcode[i] = storei
			intcode[Z] = intcode[X] + intcode[Y]
			i = i + 4
		elif intcode[i] == 2:
			intcode[i] = storei
			intcode[Z] = intcode[X] * intcode[Y]
			i = i + 4
		elif intcode[i] == 3:
			intcode[i] = storei
			intcode[X] = inpt
			i = i + 2
			if i == 2:
				return intcode, inpt, i

		elif intcode[i] == 4:
			intcode[i] = storei
			outpt = intcode[X]
			print(outpt)
			return intcode, outpt, i + 2
			i = i + 2
		elif intcode[i] == 5:
			intcode[i] = storei
			if intcode[X] != 0:
				i = intcode[Y] #
			else:
				i = i + 3 #
		elif intcode[i] == 6:
			intcode[i] = storei
			if intcode[X] == 0:
				i = intcode[Y] #
			else:
				i = i + 3 #
		elif intcode[i] == 7:
			intcode[i] = storei
			if intcode[X] < intcode[Y]:
				intcode[Z] = 1
				i = i + 4
			else:
				intcode[Z] = 0
				i = i + 4
		elif intcode[i] == 8:
			intcode[i] = storei
			if intcode[X] == intcode[Y]:
				intcode[Z] = 1
				i = i + 4
			else:
				intcode[Z] = 0
				i = i + 4
		elif intcode[i] == 99:
			intcode[i] = storei
			#print(intcode)
			print('halt!')
			i = s
			return 'halt'
