report_text = []
beacons = []
sensors = []
with open("input.txt") as input:
	for i in input: report_text.append(i.strip())

def dist(p1, p2):
	return(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))

xmax=0
for i in report_text: 
	xs=int(i.split("x=")[1].split(",")[0])
	ys=int(i.split("y=")[1].split(":")[0])
	sensors.append((xs, ys)) #drawing sensors
	xb=int(i.split("x=")[2].split(",")[0])
	yb=int(i.split("y=")[2].split(",")[0])
	beacons.append((xb, yb)) #drawing beacons
	if xs>xmax:xmax=xs
	if xb>xmax:xmax=xb

#report=zip(sensors, beacons, [dist(sensors[i], beacons[i]) for i in range(len(sensors))])

dist_max = max([dist(sensors[i], beacons[i]) for i in range(len(sensors))])


def isInRange(x,y):
	for i in range(len(sensors)):
		if dist(sensors[i], (x,y)) <= dist(sensors[i], beacons[i]) and (x,y) not in beacons:
			return(1)
	return(0)

count=0
rowq = 2000000
for x in range(0-dist_max, xmax+dist_max+1):
	count+= isInRange(x, rowq)
print("count", count)
