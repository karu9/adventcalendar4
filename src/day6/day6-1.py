## part 1 ##
values = list(map(lambda x : [int(x.split(", ")[0]), int(x.split(", ")[1])], open('input.txt').readlines()))
maxX = max([x[0] for x in values])
maxY = max([x[1] for x in values])
def closest(coord):
    dist = [abs(coord[0] - x[0]) + abs(coord[1] - x[1]) for x in values]
    mins = list(filter(lambda x : dist[x] == min(dist), range(len(values))))
    return mins[0] if len(mins) == 1 else "."
def gridgen(offset):
    grid = []
    for i in range(-offset, maxX + offset):
        for j in range(-offset, maxY + offset):
            grid.append(closest([i,j]))
    return grid
smallGrid = gridgen(3)
bigGrid = gridgen(4)
setGrid = list(set(smallGrid))
setGrid.remove(".")
print(max(list(map(lambda x : smallGrid.count(x), list(filter(lambda x : smallGrid.count(x) == bigGrid.count(x), setGrid))))))
