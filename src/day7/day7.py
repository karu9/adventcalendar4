values = [[x.split(" ")[1], x.split(" ")[7]] for x in open('input.txt').readlines()]
allSteps = sorted(list(set([x[0] for x in values] + [x[1] for x in values])))
def choice(steps, instruct, prerequisites):
    if len(steps) == 0:
        return instruct
    step = sorted(list(set(map(lambda y : y[0], filter(lambda x : len(x) == 1, prerequisites)))))[0]
    for prerequisite in prerequisites:
        if step == prerequisite[0]:
            prerequisites.remove(prerequisite)
    for prerequisite in prerequisites:
        if step in prerequisite:
            prerequisite.remove(step)
    instruct = instruct + step
    steps.remove(step)
    return choice(steps, instruct, prerequisites)
print(choice(allSteps, "", [[x] + list(set(map(lambda z: z[0], filter(lambda y : y[1] == x, values)))) for x in allSteps]))
