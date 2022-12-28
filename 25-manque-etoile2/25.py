#With the help from this Reddit comment : 
#https://www.reddit.com/r/adventofcode/comments/zur1an/comment/j1mkms7/
fuel = []
trans = {4:"-",	3:"=", 0:"0", 1:"1", 2:"2"}
trans2 = {"-":-1, "=":-2, "0":0, "1":1, "2":2}

with open("input2.txt") as input:
	for i in input:
		fuel.append(i.strip())

def SNAFUToDec(num):
	dec = 0
	for i in range(len(num)):
		if num[i] == "-": numi = -1
		elif num[i] == "=": numi = -2
		else: numi = int(num[i])
		mult = 5**(len(num)-1-i)
		dec += numi*mult
	return(dec)

def decToSNAFU(accu):
	res = ""
	while accu != 0:
		temp = trans[accu%5]
		res = temp+res
		accu = (accu - trans2[temp])/5
	return(res)

for i in range(len(fuel)):
	fuel[i] = SNAFUToDec(fuel[i])

print("Somme décimale", sum(fuel))
print("Somme SNAFU", decToSNAFU(sum(fuel)))