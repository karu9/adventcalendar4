lines = open('input.txt').readlines()
rules = [int("".join(["1" if d == '#' else "0" for d in c]), 2) for c in [[y for y in x[:5]] for x in lines]]
rulesRes = [[1 if d == '#' else 0 for d in c][0] for c in [x[x.index("=> ") + 3:x.index("=> ") + 4] for x in lines]]
print(rules)
print(rulesRes)
