# With lots of help from : https://aoc.just2good.co.uk/2022/20
from collections import deque
decryption_key = 811589153

def mix(enum):
	for index in range(len(enum)):
		while enum[0][0] != index: #have element of current index to the left
			enum.rotate(-1)
		pair = enum.popleft()
		shift = pair[1] % len(enum) #get value to move by
		enum.rotate(-shift)
		enum.append(pair)
	return(enum)

def val_at_n(values, n):
	posn = (values.index(0)+n)%len(values)
	return(values[posn])

# Opening file
with open("input2.txt") as input:
	data = list(map(int, input.read().splitlines()))

# Part 1
grove_coord = 0
mixed = mix(deque(list(enumerate(data.copy()))))
for n in (1000, 2000, 3000):
    grove_coord += val_at_n([i[1] for i in mixed], n)
print(f"Part 1: {grove_coord}")

# Part 2
mixed = deque(list(enumerate([i*decryption_key for i in data])))
for _ in range(10):
	mixed = mix(mixed)
grove_coord = 0
for n in (1000, 2000, 3000):
    grove_coord += val_at_n([i[1] for i in mixed], n)
print(f"Part 2: {grove_coord}")