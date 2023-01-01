#voir : https://aoc.just2good.co.uk/2022/21
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

with open("input2.txt") as input:
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

evaluate_monkey("root", calcs, monkeys)
print(monkeys["root"])
