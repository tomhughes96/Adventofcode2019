from itertools import permutations 

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
			


def Amp(data):
	A = 0
	perm = permutations([5, 6, 7, 8, 9]) 

	for i in list(perm):
		print(i)
		A1 = outcode(data,i[0],0)
		A2 = outcode(data,i[1],0)
		A3 = outcode(data,i[2],0)	
		A4 = outcode(data,i[3],0)	
		A5 = list(outcode(data,i[4],0))
		A5[1] = 0

		while A5 != 'halt': #until halt
			outpt = int(A5[1])
			A1 = outcode(A1[0],A5[1],A1[2])
			A2 = outcode(A2[0],A1[1],A2[2])
			A3 = outcode(A3[0],A2[1],A3[2])
			A4 = outcode(A4[0],A3[1],A4[2])
			A5 = outcode(A5[0],A4[1],A5[2])
			print(outpt)

		if outpt > A:
			A = outpt
			code = i
	print(A) 
	print(code)
	

#Amp([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5])
#Amp([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10])
Amp([3,8,1001,8,10,8,105,1,0,0,21,42,55,76,89,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,4,9,99,3,9,102,3,9,9,101,5,9,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,1001,9,5,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99])
#Amp([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])




