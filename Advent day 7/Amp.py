from itertools import permutations 

def outcode(intcode, inpt1, inpt2):
	intcode = list(intcode)
	s = len(intcode)
	i = 0
	dc = [] #output list
	k = [] #list of positions of printed instructions
	inpt = inpt1 
	outpt = 0 #starting output

	while i < s:

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
			intcode[Z] = intcode[X] + intcode[Y]
			k.append(Z)
			i = i + 4
		elif intcode[i] == 2:
			intcode[Z] = intcode[X] * intcode[Y]
			k.append(Z)
			i = i + 4
		elif intcode[i] == 3:
			intcode[X] = inpt
			k.append(X)
			inpt = inpt2 ##
			i = i + 2
		elif intcode[i] == 4:
			outpt = intcode[X]
			dc.append(outpt)
			i = i + 2
		elif intcode[i] == 5:
			if intcode[X] != 0:
				i = intcode[Y] #
			else:
				i = i + 3 #
		elif intcode[i] == 6:
			if intcode[X] == 0:
				i = intcode[Y] #
			else:
				i = i + 3 #
		elif intcode[i] == 7:
			if intcode[X] < intcode[Y]:
				intcode[Z] = 1
				k.append(Z)
				i = i + 4
			else:
				intcode[Z] = 0
				k.append(Z)
				i = i + 4
		elif intcode[i] == 8:
			if intcode[X] == intcode[Y]:
				intcode[Z] = 1
				k.append(Z)
				i = i + 4
			else:
				intcode[Z] = 0
				k.append(Z)
				i = i + 4
		elif intcode[i] == 99:
			print(intcode)
			print(outpt)
			return intcode, outpt
			i = s

def Amp(data):
	A = 0
	perm = permutations([0, 1, 2, 3, 4]) 
	for i in list(perm):
		A1 = outcode(data,i[0],0)
		A2 = outcode(data,i[1],A1[1])
		A3 = outcode(data,i[2],A2[1])
		A4 = outcode(data,i[3],A3[1])
		A5 = outcode(data,i[4],A4[1])
		print(A5[1])
		if A5[1] > A:
			A = A5[1]
			code = i
	print(A) 
	print(code)
	

#Amp([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])
Amp([3,8,1001,8,10,8,105,1,0,0,21,42,55,76,89,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,4,9,99,3,9,102,3,9,9,101,5,9,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,1001,9,5,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99])
#outcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],100,100)
#outcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1],100,100)

#answer
#20413


