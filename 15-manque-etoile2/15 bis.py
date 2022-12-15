report_text = []
beacons = []
sensors = []

with open("input.txt") as input:
	for i in input: report_text.append(i.strip())

def dist(p1, p2):
	return(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))

for i in report_text: 
	xs=int(i.split("x=")[1].split(",")[0])
	ys=int(i.split("y=")[1].split(":")[0])
	sensors.append((xs, ys)) #drawing sensors

	xb=int(i.split("x=")[2].split(",")[0])
	yb=int(i.split("y=")[2].split(",")[0])
	beacons.append((xb, yb)) #drawing beacons

def isInRange(x,y):
	for i in range(len(sensors)):
		if dist(sensors[i], (x,y)) <= dist(sensors[i], beacons[i]):
			return(True)
	return(False)

print("start!")
for x in range(4000001):
	for y in range(4000001):
		if not isInRange(x,y):
			if (x,y) not in beacons and (x,y) not in sensors:
				print("pas in range", x, y)
				print("Tuning frequency :", x*4000000+y)
	print(x)
