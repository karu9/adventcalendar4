lines = open('input.txt').readlines()
rules = [[y for y in x[:5]] for x in lines]
rulesRes = [x[x.index("=> ") + 3:x.index("=> ") + 4] for x in lines]
plants = [x for x in "......................#....##.#.#.####..#.######..##.#.########..#...##...##...##.#.#...######.###....#...##..#.#....##.##......................"]
for i in range(20):
    lp = len(plants)
    result = ["."] * lp
    for j in range(2, lp-1):
        currplant = plants[j-2:j+3]
        if currplant in rules:
            result[j] = rulesRes[rules.index(currplant)]
    plants = result
count = 0
for i in range(len(plants)):
    if plants[i] == "#":
        count = count - 22 + i
print(count)
