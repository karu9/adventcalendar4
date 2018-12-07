lines = open('input.txt').readlines()
twos = 0
threes = 0
for line in lines:
    twos = twos + 1 if not len(list(filter(lambda x : line.count(x) == 2, line))) == 0 else twos
    threes = threes + 1 if not len(list(filter(lambda x : line.count(x) == 3, line))) == 0 else threes
print(twos * threes)
for i in range(len(lines)):
    for line in lines[i:]:
        count = 0
        for j in range(len(line)):
            if not lines[i][j] == line[j]:
                count = count + 1
        if count == 1:
            print(line)
            print(lines[i])
            
