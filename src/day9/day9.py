np = 418
nb = 70770
scores = [0 for i in range(np)]
pos = 0
circle = [0]
player = 1
for i in range(1, nb):
    player = (player + 1) % np
    if i % 23 == 0 :
        pos = (pos - 7) % len(circle)
        scores[player] = scores[player] + i + circle[pos]
        circle = circle[:pos] + circle[pos+1:]
    else :
        pos = (pos + 2) % len(circle)
        circle = circle[:pos] + [i] + circle[pos:]
print(max(scores), scores.index(max(scores)))
