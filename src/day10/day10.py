## part 1 ##
lines = open('input.txt').readlines()
pos = [[int(x[x.index("<")+1:x.index(', ')]), int(x[x.index(", ")+2:x.index('> v')]), int(x[x.index("y=<")+3:x[x.index(', ')+3:].index(', ')+x.index(', ')+3]), int(x[x[x.index(', ')+3:].index(', ')+x.index(', ')+3+2: -2])] for x in lines]
def printGrid(positions):
    xs = [x[0] for x in positions]
    ys = [y[1] for y in positions]
    minX = min(xs)
    maxX = max(xs)
    minY = min(ys)
    maxY = max(ys)
    xys = [[x[0], x[1]] for x in positions]
    grid = []
    for j in range(minY, maxY+1):
        subgrid = []
        grid.append(subgrid)
        for i in range(minX, maxX+1):
            if [i,j] in xys:
                subgrid.append("#")
            else:
                subgrid.append(".")
    for x in grid:
        print(x)
def move(position, n):
    return [[x[0]+ n* x[2], x[1] + n * x[3], x[2], x[3]] for x in position]
i = 10100
while True:
    currPos = move(pos, i)
    if max([y[1] for y in currPos]) - min([y[1] for y in currPos]) == 9:
        print(i)
        printGrid(currPos)
        break
    else :
        print(max([y[1] for y in currPos]) - min([y[1] for y in currPos]))
    i = i + 1
