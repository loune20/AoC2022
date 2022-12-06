datastream = []
with open("input.txt") as input:
	for i in input.readline().strip():
		datastream.append(i)

marker = datastream[0:14]

for i in range(14, len(datastream)):
	marker.pop(0)
	marker.append(datastream[i])
	if len(set(marker)) == len(marker):
		chara = i+1
		break
print(chara)