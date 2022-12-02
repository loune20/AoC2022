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
    score += score_shape.index(round[2])+1
    return(score)

def playShape(round):
    if round[2] == "Y": #draw
       shape = draw[1][draw[0].index(round[0])]
    elif round[2] == "X": #defeat
        shape = defeat[1][defeat[0].index(round[0])]
    elif round[2] == "Z": #win
        shape = win[1][win[0].index(round[0])]
    return(round[0:2]+shape)

print(sum([scoreRound(playShape(t)) for t in guide]))