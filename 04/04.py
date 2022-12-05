pairs = []
count1 = 0
count2 = 0
with open("input.txt") as input:
	for i in input:
		pairs.append(i.strip())

for i in range(len(pairs)):
	p1 = [0, 0, set()]
	p2 = [0, 0, set()]
	p1[0] = int(pairs[i].split("-")[0])
	p1[1] = int(pairs[i].split("-")[1].split(",")[0])
	p2[0] = int(pairs[i].split("-")[1].split(",")[1])
	p2[1] = int(pairs[i].split("-")[2])
	for j in range(p1[0], p1[1]+1):
		p1[2].add(j)
	for j in range(p2[0], p2[1]+1):
		p2[2].add(j)
	#print("Ligne", i, ":", p1[2], p2[2])
	if p1[2]|p2[2] == p2[2] or p1[2]|p2[2]== p1[2]:
		count1+=1
	if p1[2] & p2[2]:
		count2+=1

print(count1, count2)