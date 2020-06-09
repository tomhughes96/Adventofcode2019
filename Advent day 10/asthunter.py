def astcoords(map,w,h): #grid is w by h
	grid = []
	K = []
	coords1 = [] #coords of asteroids
	cansee = 0

	for i in range(0,h): #parse map into rows
		grid.append(map[i*w:(i+1)*w])
	for i in range(0,h):
		for j in range(0,w):
			if grid[i][j] == '#':
				coords1.append([j,i])
	
	for i in coords1:
		differences = [] #list of differences
		pos = [] #list of positive y coords
		neg = [] #list of positive x coords
		for j in coords1:
			C1 = [j[0]-i[0], j[1] - i[1]]
			differences.append(C1) 
		differences.remove([0,0])
		for k in differences:
			if k[0] > 0:
				pos.append(k[1]/k[0])
			if k[0] < 0:
				neg.append(k[1]/k[0])
			if k[0] == 0:
				if k[1] > 0:
					pos.append(1000)
				if k[1] < 0:
					neg.append(-1000)

		pos = list(dict.fromkeys(pos)) #gets rid of duplicates
		neg = list(dict.fromkeys(neg)) #gets rid of duplicates
		pos.sort(reverse=True) #order
		neg.sort() #order
		
		if len(pos) + len(neg) > cansee:
			cansee = len(pos) + len(neg)
			coord = i
			print(cansee) #number of seen asteroids
			print(i) #coord of current best meteor
			M = pos + neg #concatenated list
			print(M[199]) #200th meteor (less than one full rotation)
		for k in differences:
			if k[0] == 0:
				1+1
			elif k[1]/k[0] == M[199]:
				print(k) #+-[16,9]
				#[19,14] - [16,9] = [3,5]
				#3 * 100 + 5 = 305

		
astcoords('.##.#.#....#.#.#..##..#.#.#.##.#..#.####.##....##.#.###.##.##.#.#...#..###....####.##..###.#.#...####..#..#####..#.#.#..#######..#.###..##..###.####.#######.##..##.###..##.##.....####..#..###..##.#...#..####.....#.#...##.##....#.#..##..#.#.###.####..##.###.#.#.#..##.#####.##.####..#.#.#..##.#.#.###.#..##.##....#.#.##.#.##.##......###.#.#####...###.####..#.##.....#####.#.#..#.##.#.#...###.#..#.##.#.#.##.#....###.#.......###.#....##.....####..#####.#..#..##..##.#.####.#.###..######.###..#..##.#....####.##.###....####..#.#.#.########.....#.#.#.##.#.#..#...###.####..##.##...###....#.##.##..#......##.##.##.#######..#...#..###..#.#..#...###..###.#.#..#..#######..#.#..#..#.#',26,26)


#answers
#273
#305