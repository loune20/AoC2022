datastream = []
with open("input.txt") as input:
	for i in input.readline().strip():
		datastream.append(i)

marker = datastream[0:4]

for i in range(3, len(datastream)):
	marker.pop(0)
	marker.append(datastream[i+1])
	if len(set(marker)) == len(marker):
		chara = i+2
		break
print(chara)