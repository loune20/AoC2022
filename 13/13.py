import json
pdata = []
pairs = []
with open("input2.txt") as input:
	for i in input:
		pdata.append(i.strip())

for i in range(0, len(pdata), 3):
	pairs.append([json.loads(pdata[i]), json.loads(pdata[i+1])])

for i in pairs:print(i)
print("---")

def compList(lleft, lright):
	for i in range(len(lright)):
		if i>=len(lleft): #pas d'items dans liste de gauche à comparer
			print("lgauche vide")
			return(True)
		elif i>=len(lright): #pas d'items dans liste de droite à comparer
			print("ldroite vide")
			return(False)
		else:
			if compInt(lleft[i], lright[i]) == False:print(i,"igauche>idroite");return(False)
			elif compInt(lleft[i], lright[i]) == True:print(i,"idroite>igauche");return(True)
	print("??")

def compInt(ileft, iright):
	if ileft<iright:return(True)
	elif ileft>iright:return(False)
	else: return("cont")

def checkFormat(left, right):
	if type(left) == type(right):
		if type(left) == list:
			print("list!")
			a=[True for i in left if type(i) == list]+([True for i in right if type(i) == list])
			print(a)
			#print(compList(left, right))
		elif type(pair[0]) == int:
			print("int!")
			#print(compInt(left, right))
	else:
		print("mixed type")


for pair in pairs:
	print(pairs.index(pair), "-", pair[0], " ", pair[1])
	checkFormat(pair[0], pair[1])
	print("--")