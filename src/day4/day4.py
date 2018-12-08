lines = open('input.txt').readlines()
# link day with guard number #
guards = sorted(list(map(lambda x : [x[3][1:], x[0][1:]], list(filter(lambda y: y[2] == "Guard", [x.split(" ") for x in lines])))))
# fill with sleep / up time #
for guard in guards:
    day = guard[1]
    times = []
    for line in lines :
        l = line.split(" ")
        if l[0][1:] == day:
            if l[2] == "Guard":
                continue
            elif l[2] == "falls":
                times.append([int(l[1][3:-1]), False])
            else :
                times.append([int(l[1][3:-1]), True])
    times = sorted(times)
    if len(times) == 0 or not times[0][0] == 0:
        times = [[0, 1]] + times
    minutesAsleep = []
    status = True
    for i in range(0,60):
        for time in times:
            if i == time[0]:
                status = time[1]
                break
        if not status :
            minutesAsleep.append(i)
    guard.append(minutesAsleep)
guardIds = list(set(map(lambda x : x[0], guards)))
minutes = []
for guardId in guardIds:
    minu = []
    for minute in list(map(lambda y: y[2], filter(lambda x: x[0] == guardId, guards))):
        minu = minu + minute
    minutes.append(minu)
ms = [len(x) for x in minutes].index(max([len(x) for x in minutes]))
mst = minutes[ms]
print(guardIds)
print(guardIds[ms])
mostSlept = mst[[mst.count(x) for x in mst].index(max([mst.count(x) for x in mst]))]
print(mostSlept)
print(int(guardIds[ms]) * mostSlept)
        

    
