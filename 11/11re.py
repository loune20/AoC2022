import re
_monk = []
monkeys = []
with open("input2.txt") as input:
	for i in input: _monk.append(i.strip())

class Monkey:
	def __init__(self, source):
		self.source = source
		self.id = re.search("\d", source[0]).group()
		self.items = re.search("\d", source[1]).group()

for i in range(0, len(_monk), 7):
	print(a:=_monk[i:i+6])
	monkeys.append(Monkey(a))

print(monkeys[1].items)