lines = open('input.txt').readlines()
coords = []
for i in lines :
    x = int(i.split(" @ ")[1].split(": ")[0].split(",")[0])
    y = int(i.split(" @ ")[1].split(": ")[0].split(",")[1])
    deltax = int(i.split(" @ ")[1].split(": ")[1].split("x")[0])
    deltay = int(i.split(" @ ")[1].split(": ")[1].split("x")[1])
    coords.append([x,x+deltax-1,y,y+deltay-1])
overlaps = []
for i in range(len(coords)):
    print(i)
    for j in range(i+1, len(coords)):
        overlapX = list(filter(lambda x : x in range(coords[j][0], coords[j][1]+1), range(coords[i][0], coords[i][1]+1)))
        if len(overlapX) == 0:
            continue
        overlapY = list(filter(lambda y : y in range(coords[j][2], coords[j][3]+1), range(coords[i][2], coords[i][3]+1)))
        if len(overlapY) == 0:
            continue
        for x in overlapX:
            for y in overlapY:
                co = str(x) + "," + str(y)
                overlaps.append(co)
print(len(set(overlaps)))
def overlap(coord, overlaps):
    for i in range(coord[0], coord[1]+1):
        for j in range(coord[2], coord[3]+1):
            co = str(i) + "," + str(j)
            if co in overlaps:
                return True
    return False
            
for i in range(len(coords)):
    print(i)
    if not overlap(coords[i], overlaps):
        print("result ", i+1)
        break
    
            
