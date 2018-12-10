## part 1 ##
values = list(map(lambda x : [int(x.split(", ")[0]), int(x.split(", ")[1])], open('input.txt').readlines()))
maxX = max([x[0] for x in values])
maxY = max([x[1] for x in values])
def sumGrid(coord):
    dist = [abs(coord[0] - x[0]) + abs(coord[1] - x[1]) for x in values]
    return "#" if sum(dist) < 10000 else "."
def gridgen(offset):
    grid = []
    for i in range(-offset, maxX + offset):
        for j in range(-offset, maxY + offset):
            grid.append(sumGrid([i,j]))
    return grid
smallGrid = gridgen(0)
print(smallGrid.count("#"))
