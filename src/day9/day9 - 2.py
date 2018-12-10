np = 418
nb = 70769 + 1
scores = [0 for i in range(np)]
circle = [0]
player = 1
for i in range(1, nb):
    player = (player + 1) % np
    if i % 23 == 0 :
        scores[player] = scores[player] + i + circle[-7]
        circle = circle[-6:] + circle[:-7] 
    else :
        circle = [i] + circle[2:] + circle[:2]  
    if i % 10000 == 0:
        print(i)
print(max(scores), scores.index(max(scores)))
