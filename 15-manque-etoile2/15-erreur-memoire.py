report_text = []
zone = {}
beacons = []
sensors = []
with open("input2.txt") as input:
	for i in input: report_text.append(i.strip())

def printZone():
	all_x, all_y = [], []
	for key in zone.keys():
		if key[0] not in all_x: all_x.append(key[0])
		if key[1] not in all_y: all_y.append(key[1])
	all_y.sort()
	print("x allant de", min(all_x), "à", max(all_x))
	for y in all_y:
		line = []
		for x in range(min(all_x), max(all_x)+1):
			if (x,y) in zone:
				line.append(zone[x,y])
			else:
				line.append(".")
		if len(str(y))==1:y="0"+str(y)
		print(y,"".join(line))

def dist(p1, p2):
	return(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))

for i in report_text: 
	xs=int(i.split("x=")[1].split(",")[0])
	ys=int(i.split("y=")[1].split(":")[0])
	sensors.append((xs, ys))
	zone[xs,ys] = "S" #drawing sensors
	xb=int(i.split("x=")[2].split(",")[0])
	yb=int(i.split("y=")[2].split(",")[0])
	beacons.append((xb, yb))
	zone[xb,yb] = "B" #drawing beacons

printZone()

minY = min([key[1] for key in zone.keys()])
for s_index in range(len(sensors)):
	#print(sensors[s_index], beacons[s_index], dist(sensors[s_index], beacons[s_index]))
	distA = dist(sensors[s_index], beacons[s_index])
	top = sensors[s_index][1]-distA
	bottom = sensors[s_index][1]+distA
	for j in range(top, bottom+1):
		diff=j-sensors[s_index][1]
		if diff>0:
			fact=abs(j-(sensors[s_index][1]+distA))
		else: 
			fact=abs(j-(sensors[s_index][1]-distA))
		#print("j",j, "; diff", diff, "fact", fact)
		for m in range(-fact, fact+1):
			if (sensors[s_index][0]+m, j) not in zone:
				zone[sensors[s_index][0]+m, j] = "#"
printZone()
print([(value) for key, value in zone.items() if key[1]==2000000].count("#"))
