#solved with help from : https://aoc.just2good.co.uk/2022/21
import re
import operator

monkeys = {}
calcs = {}
opMap = {
	"+":operator.add,
	"*":operator.mul,
	"-":operator.sub,
	"/":operator.floordiv
	}

with open("input.txt") as input:
	yell_pattern = re.compile(r"([a-z]{4}): (\d+)")
	calc_pattern = re.compile(r"([a-z]{4}): ([a-z]{4}) (.){1,2} ([a-z]{4})")
	for i in input:
		if match := yell_pattern.match(i):
			monkeys[match.groups()[0]] = int(match.groups()[1])
		elif match := calc_pattern.match(i):
			calcs[match.groups()[0]] = (match.groups()[1], match.groups()[2], match.groups()[3])

def evaluate_monkey(monkey_id, calcs, monkeys):
	assert monkey_id in calcs, "Monkey must have an operation"
	current_calc = calcs[monkey_id]
	monkey2, monkey3 = current_calc[0], current_calc[2]
	op = current_calc[1]

	if monkey2 not in monkeys:
		evaluate_monkey(monkey2, calcs, monkeys)
	if monkey3 not in monkeys:
		evaluate_monkey(monkey3, calcs, monkeys)

	monkeys[monkey_id] = opMap[op](monkeys[monkey2], monkeys[monkey3])
	return monkeys[monkey_id]

def try_monkeys(candidate, calcs, monkeys): #return root for humn = candidate
	monkeys_try = monkeys.copy()
	monkeys_try["humn"] = candidate
	res = evaluate_monkey("root", calcs, monkeys_try)
	return(res)


# Part 2
#set the operator for root as minus : if the result is 0, both monkeys are equal
calcs["root"] = (calcs["root"][0], "-", calcs["root"][2])

#try monkeys until solution found...
candidate = 3343167719430
res = None
while res != 0:
	candidate += 1
	res = try_monkeys(candidate, calcs, monkeys)
	if candidate > 3343167719440: break
	if candidate%1 == 0:print(candidate)
print(candidate)

#solved using lots of time :3343167719435
