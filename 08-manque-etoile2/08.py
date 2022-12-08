patch = []
with open("input.txt") as input:
	loop=0
	for i in input:
		patch.append([])
		for j in i.strip():
			patch[loop].append([int(j), "Unknown"])
		loop+=1

# Edges trees
for i in patch:i[0][1] = True; i[-1][1] = True #Right  and left column trees
for i in patch[0]:i[1]=True #Top row trees
for i in patch[-1]:i[1]=True #Bottom row trees

# Looking from left of the forest (looping right to left)
for tree_row in patch:
	for i_tree in range(1, len(tree_row)-1):
		#print(tree_row[i_tree])
		for j in range(i_tree-1, -1, -1):
			if tree_row[j][0] < tree_row[i_tree][0]: # L'arbre j est plus petit que l'arbre examiné
				if j==0: # Cet arbre est le dernier de la rangée, le plus à droite
					tree_row[i_tree][1] = True
			else:
				break
	#print("--")

# Looking from right of the forest (looping left to right)
for tree_row in patch:
	for i_tree in range(1, len(tree_row)-1):
		#print(tree_row[i_tree])
		for j in range(i_tree+1, len(tree_row), 1):
			if tree_row[j][0] < tree_row[i_tree][0]: # L'arbre j est plus petit que l'arbre examiné
				if j==len(tree_row)-1: # Cet arbre est le dernier de la rangée, le plus à droite
					tree_row[i_tree][1] = True
			else:
				break
	#print("--")

# Looking from bottom (looping from bottom to top)
for col in range(len(patch)):
	for row in range(len(patch)):
		#print(patch[row][col])
		for i in range(len(patch)-1, row, -1):
			if patch[i][col][0] < patch[row][col][0]: # plus petit
				if i == row+1: # fin de rangée
					patch[row][col][1] = True
			else:
				break
	#print("--")

# Looking from top (looping from bottom to top too)
for col in range(len(patch)):
	for row in range(len(patch)):
		#print(patch[row][col])
		for i in range(row-1, -1, -1):
			if patch[i][col][0] < patch[row][col][0]: #plus petit
				if i == 0: #fin de rangée
					patch[row][col][1] = True
			else:
				break
	#print("--")


#for i in patch:print(i)

#Print visible trees
print("Somme des arbres visibles :", sum([[j[1] for j in i].count(True) for i in patch]))