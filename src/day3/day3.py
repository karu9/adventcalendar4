lines = open('input.txt').readlines()
coords = []
for i in lines :
    x = int(i.split(" @ ")[1].split(": ")[0].split(",")[0])
    y = int(i.split(" @ ")[1].split(": ")[0].split(",")[1])
    deltax = int(i.split(" @ ")[1].split(": ")[1].split("x")[0])
    deltay = int(i.split(" @ ")[1].split(": ")[1].split("x")[1])
    coords.append([x,x+deltax,y,y+deltay])
minX = min(list(map(lambda x : x[0], coords)))
maxX = max(list(map(lambda x : x[1], coords)))
minY = min(list(map(lambda x : x[2], coords)))
maxY = max(list(map(lambda x : x[3], coords)))
print(maxX)
print(maxY)

count = 0
for i in range(minX, maxX+1):
    print(i)
    for j in range(minY, maxY+1):
        l = 0
        for coord in coords :
            if coord[0] <= i and coord[1] >= i and coord[2] <= j and coord[3] >= j:
                l = l + 1
            if l > 1 :
                count = count + 1
                break
print(count)
