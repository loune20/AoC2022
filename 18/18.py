scan = []

with open("input.txt") as input:
	for i in input:
		scan.append(tuple(map(int, i.split(","))))

def calcExp(cube):
	x = cube[0]
	y = cube[1]
	z = cube[2]
	exp = 6
	if (x,y,z+1) in scan: #face A/devant
		exp -= 1
	if (x+1,y,z) in scan: #face B/droite
		exp -= 1
	if (x,y,z-1) in scan: #face C/derrière
		exp -= 1
	if (x-1,y,z) in scan: #face D/gauche
		exp -= 1
	if (x,y+1,z) in scan: #face E/haut
		exp -= 1
	if (x,y-1,z) in scan: #face F/bas
		exp -= 1
	return(exp)

print("Étoile 1 :",sum([calcExp(i) for i in scan]))
