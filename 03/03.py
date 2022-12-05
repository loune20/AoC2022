rs = []
rs2 = []
item = []
pri_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = []

with open("input.txt") as input:
	for i in input:
		rs.append(i.strip())

for i in range(len(rs)):
	rs2.append([{},{}])
	rs2[i][0] = set(rs[i][0:int(len(rs[i])/2)])
	rs2[i][1] = set(rs[i][int(len(rs[i])/2):int(len(rs[i]))])
	for i in rs2[i][0] & rs2[i][1]:item.append(i)

for i in item:priority.append(pri_list.index(i)+1)
print(sum(priority))