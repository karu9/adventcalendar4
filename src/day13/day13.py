track = [x[:-1] for x in open('input.txt').readlines()]
initcartpos = []
for i in range(len(track)):
    for j in range(len(track[0])):
        if track[j][i] in "<>v^":
            initcartpos.append([i,j, "<>v^".index(track[j][i]), 0])
print(initcartpos)
def move(cartpos):
    rescartpos = []
    for pos in cartpos:
        direction = pos[2]
        nextPos = []
        if direction == 0:
            nextPos = [pos[0]-1, pos[1], direction, pos[3]]  
        elif direction == 1:
            nextPos = [pos[0]+1, pos[1], direction, pos[3]]  
        elif direction == 2:
            nextPos = [pos[0], pos[1]+1, direction, pos[3]]  
        else:
            nextPos = [pos[0], pos[1]-1, direction, pos[3]]
        nexttrack = track[nextPos[1]][nextPos[0]]
        if nexttrack == "+" :
            mod = nextPos[3] % 3
            nextPos[3] = mod + 1
            #turn left#
            if mod == 0 :
                if direction == 0 :
                    nextPos[2] = 2
                elif direction == 1 :
                    nextPos[2] = 3
                elif direction == 2 :
                    nextPos[2] = 1
                else :
                    nextPos[2] = 0
            if mod == 2:
                if direction == 0 :
                    nextPos[2] = 3
                elif direction == 1 :
                    nextPos[2] = 2
                elif direction == 2 :
                    nextPos[2] = 0
                else :
                    nextPos[2] = 1
        elif nexttrack == "/" :
            if direction == 0 :
                nextPos[2] = 2
            elif direction == 1 :
                nextPos[2] = 3
            elif direction == 2 :
                nextPos[2] = 0
            else :
                nextPos[2] = 1
        elif nexttrack == "\\" :
            if direction == 0 :
                nextPos[2] = 3
            elif direction == 1 :
                nextPos[2] = 2
            elif direction == 2 :
                nextPos[2] = 1
            else :
                nextPos[2] = 0
        rescartpos.append(nextPos)
    return rescartpos
laps = 0
while True:
    positions = [x[:2] for x in initcartpos]
    dups = [x for x in positions if positions.count(x) > 1]
    if len(dups) != 0:
        print(dups, laps)
        break
    initcartpos = move(initcartpos)
    laps = laps + 1
