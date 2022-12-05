start = []
proced = []
stacks = []
max_stacks = 9 #modifier selon input
top_crates = ""

with open("input.txt") as input:
	a=True
	for i in input:
		if a==True:start.append(i)
		if a==False:proced.append(i.strip())
		if i.strip()=="":a=False

for i in range(max_stacks):stacks.append([])

for i in range(1, max_stacks+1):
	index = start[-2].find(str(i))
	for j in range(len(start)-2):
		if start[j][index] != " ":
			stacks[i-1].append(start[j][index])

def move(qt, start, end):
	#copier stacks à déplacer dans ordre
	crates = stacks[start-1][0:qt]
	#supprimer stacks ancienne liste
	for i in range(qt):
		stacks[start-1].pop(0)
	#copier stacks dans nouvelle liste
	for i in range(len(crates)):
		stacks[end-1].insert(0, crates[(i*-1)-1])

for i in range(len(proced)): #ou len(proced)-1 si pas de ligne en fin
	qt = int(proced[i].split("move ")[1][:2].strip())
	start = int(proced[i].split("from ")[1][0])
	end = int(proced[i].split("to ")[1][0])
	move(qt, start, end)


for i in range(len(stacks)):
	if stacks[i] != []:
		top_crates = top_crates + stacks[i][0]
print(top_crates)

