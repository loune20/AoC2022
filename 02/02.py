guide = []
draw = [("A", "B", "C"), ("X", "Y", "Z")]
win = [("A", "B", "C"), ("Y", "Z", "X")] #win for me, defeat for opponent
defeat = [("A", "B", "C"), ("Z", "X", "Y")]
score_shape = ("X", "Y", "Z")

with open("input.txt") as input:
    for i in input: guide.append(i.strip())

def scoreRound(round):
    score=0
    if draw[0].index(round[0]) == draw[1].index(round[2]):
        score += 3
    elif win[0].index(round[0]) == win[1].index(round[2]):
        score += 6
    #elif defeat[0].index(round[0]) == defeat[1].index(round[2]):
        #print("defeat")
    score += score_shape.index(round[2])+1
    return(score)

score = sum([scoreRound(t) for t in guide])
print(score)   



