rs = []
rs2 = []
item = []
pri_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = []

with open("input.txt") as input:
	for i in input:
		rs.append(i.strip())
j=0
for i in range(0, len(rs),3):
	rs2.append([])
	rs2[j].append(set(rs[i]))
	rs2[j].append(set(rs[i+1]))
	rs2[j].append(set(rs[i+2]))
	for i in (rs2[j][0] & rs2[j][1] & rs2[j][2]):item.append(i)
	j+=1

for i in item:priority.append(pri_list.index(i)+1)
print(sum(priority))