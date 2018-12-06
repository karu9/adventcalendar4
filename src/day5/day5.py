## part 1 ##
inp = open('input.txt').readlines()[0]
def reduc(text):
    dups = []
    x = 0
    while x < len(text) - 1:
        if text[x].lower() == text[x+1].lower() and not text[x] == text[x+1]:
            dups.append(x)
            x = x + 1
        x = x + 1
    for y in dups[::-1] :
        text = text[:y] + text[y+2:]
    return text
while True:
    l = len(inp)
    inp = reduc(inp)
    if l == len(inp):
        break
print(len(inp))

    
