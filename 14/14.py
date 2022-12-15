scan = []
cave = {}
sand_count = 0

with open("input.txt") as input:
	for i in input:
		scan.append(i.strip())

def fillRock(depart, arrivee):
	if depart[0] == arrivee[0]: #vertical
		if depart[1] > arrivee[1]: #baisse
			xa, xd = depart[1], arrivee[1]
		else: #hausse
			xd, xa = depart[1], arrivee[1]
		for i in range(xd, xa+1):
			cave[(depart[0], i)] = "#"

	elif depart[1] == arrivee[1]: #horizontal
		if depart[0] > arrivee[0]: #baisse
			xd, xa = depart[0], arrivee[0]
		else: #hausse
			xa, xd = depart[0], arrivee[0]
		for i in range(xa, xd+1):
				cave[(i, depart[1])] = "#"
	else:
		print("erreur")

def printCave():
	xs, ys = [], []
	for key, value in cave.items():
		if key[1] not in ys: ys.append(key[1])
		if key[0] not in xs: xs.append(key[0])
	xs.sort()
	ys.sort()
	print("début",min(xs),"fin",max(xs))
	for y in ys:printCaveWithAir(y, xs)

def printCaveWithAir(y, xs):
	output = []
	for x in range(min(xs), max(xs)+1):
		if (x,y) in cave:
			output.append(cave[x,y])
		else:
			output.append(".")
	print(y, "".join(output))

def addSand(x, y):
	depass=False
	while True:
		if y+1>y_max:
			return(False)
		if (x, y+1) not in cave: #down
			y+=1
		elif (x-1, y+1) not in cave: #down left
			x-=1
			y+=1
		elif (x+1, y+1) not in cave: #down right
			x+=1
			y+=1
		else:
			cave[x,y] = "o"
			return(True)

# Fill the cave with rock path
for i in scan:
	for j in range(i.count("->")):
		depart = tuple([int(i) for i in (i.split("->")[j].strip()).split(",")])
		arrivee = tuple([int(i) for i in (i.split("->")[j+1].strip()).split(",")])
		fillRock(depart, arrivee)
cave[500,0] = "+" #add sand pouring origin
y_max = max([key[1] for key in cave.keys()])

# Adding sand and printing the cave
print("start cave :")
printCave()
print("adding sand...\n")

while addSand(500,0) == True:
	sand_count+=1
print("all sand now fall into the void")
print("\nSand count :",sand_count)