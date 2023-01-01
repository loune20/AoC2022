doneMonkeys = []
calcMonkeys = []

with open("input.txt") as input:
	for i in input:
		if len(i.strip().split(": ")[1])<4:
			doneMonkeys.append({
				"name":i.split(":")[0],
				"num":int(i.strip().split(": ")[1])
				})
		else:
			calcMonkeys.append({
				"name":i.split(":")[0],
				"num1":i.split(": ")[1][0:4],
				"num2":i.split(": ")[1][7:11],
				"oper":i.split(": ")[1][5]
				})

while calcMonkeys != []:
	for monk in calcMonkeys:
		resultat=""
		if (monk["num1"] in [m["name"] for m in doneMonkeys]) and (monk["num2"] in [m["name"] for m in doneMonkeys]):
			m1 = [m for m in doneMonkeys if m["name"]==monk["num1"]][0]["num"]
			m2 = [m for m in doneMonkeys if m["name"]==monk["num2"]][0]["num"]
			oper = monk["oper"]
			match oper:
				case "+":resultat=m1+m2
				case "-":resultat=m1-m2
				case "*":resultat=m1*m2
				case "/":resultat=m1/m2
			doneMonkeys.append({"name":monk["name"],"num":resultat})
			calcMonkeys.remove(monk)

print(int([m for m in doneMonkeys if m["name"]=="root"][0]["num"]))
