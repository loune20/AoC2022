monkeys = []
ic = []
with open("input2.txt") as input:
	for i in input:
		ic.append(i)

for i in range(len(ic)):
	if ic[i][:7] == "Monkey ":
		monkeys.append({
			"id":int(ic[i].split()[1].split(":")[0]), 
			"items":[int(it.strip()) for it in ic[i+1].split(": ")[1].split(", ")],
			"opé" : ic[i+2].split(": ")[1].split()[3:5],
			"test" : int(ic[i+3].split("by ")[1]),
			"true" : int(ic[i+4].split("monkey ")[1]),
			"false" : int(ic[i+5].split("monkey ")[1]),
			})

"""for i in monkeys:
	for (key, value) in i.items():
		print(key, value)
	print("--")"""

def turn(id):
	m = monkeys[id]
	for item in m["items"]:
		worry = item
		print(worry, item)
		#print("Item worry level :",worry) #inspected item
		worry = eval(str(worry)+"".join(m["opé"]).replace("old", str(worry))) #worry updates accordingly with operation
		#print("Worry after op:", worry)
		worry //= 3 #monkey got bored
		#print("Worry after monkey got bored:", worry)
		if worry%m["test"] == 0: #test item and throw to other monkey
			monkeys[m["true"]]["items"].append(worry)
			monkeys[id]["items"].remove(item)
			print("test true, item worry level",worry, "thrown to monkey", monkeys[m["true"]]["id"])
		else:
			monkeys[m["false"]]["items"].append(worry)
			monkeys[id]["items"].remove(item)
			print("test false, item worry level",worry, "thrown to monkey", monkeys[m["false"]]["id"])
		
		print("--")
	print(monkeys[id]["items"])#.remove(item)
		
for i in range(len(monkeys)):
	print("Monkey",i)
	turn(i)
	print("···")

for i in monkeys:
	print(i["id"], i["items"])
