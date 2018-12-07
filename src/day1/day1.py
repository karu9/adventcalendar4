lines = list(map(lambda x : eval(x), open('input.txt').readlines()))
total = [sum(lines[:x+1]) for x in range(0, len(lines))][-1]
print(total)
i = 0
values = [0]
while True:
    nextVal = values[-1] + lines[i]
    i = (i + 1) % len(lines)
    if nextVal in values :
        print(nextVal)
        break
    values.append(nextVal)
    
