cal_count = [0]
a = 0
with open("input.txt") as input:
    for i in input:
        if i != "\n":
            cal_count[a] += int(i.strip())
        else:
            cal_count.append(0)
            a += 1
print(sum(sorted(cal_count)[-3:]))