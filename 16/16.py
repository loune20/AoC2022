report = {}

class Valve:
	def __init__(self, name, flow, leadsto):
		self.name = name
		self.flow = flow
		self.leadsto = leadsto

	def __str__(self):
		return f"Valve {self.name} - flow rate : {self.flow}, leads to : {self.leadsto}"

with open("input2.txt") as input:
	for i in input:
		report[i[6:8]] = Valve(
			i[6:8],
			int(i.split("=")[1].split(";")[0]),
			[v.replace(",", "") for v in i.split("to valv")[1].split()[1:]])

for v in report.values():print(v)

def pressureReleased(valves_names):
	print("Somme",sum([report[v].flow for v in valves_names]), "flow",[report[v].flow for v in valves_names])
	return(sum([report[v].flow for v in valves_names]))	

def minute(min_curr, valv_curr, open_valves):
	

pressureReleased(["AA", "BB"])

