def extract(words):
    x, y = (int(k) for k in words[2][:-1].split(','))
    w, h = (int(k) for k in words[3].split('x'))
    n = words[0][1:]
    return x, y, w, h, n

def partone(file):
    patches = [extract(line.strip().split()) for line in file]
    s = set()
    for n, p2 in enumerate(patches):
        for p1 in patches[:n]:
            for x in range(max(p1[0],p2[0]),min(p1[0]+p1[2],p2[0]+p2[2])):
                for y in range(max(p1[1],p2[1]),min(p1[1]+p1[3],p2[1]+p2[3])):
                    s.add((x,y))
    return len(s)
                                
def parttwo(file):
    patches = [extract(line.strip().split()) for line in file]
    intact = set(p[4] for p in patches)
    for n, p2 in enumerate(patches):
        for p1 in patches[:n]:
            if max(p1[0],p2[0]) < min(p1[0]+p1[2],p2[0]+p2[2])\
            and max(p1[1],p2[1]) < min(p1[1]+p1[3],p2[1]+p2[3]):
                intact.discard(p1[4])
                intact.discard(p2[4])
    return intact
    
with open('input.txt') as f:
    print(partone(f))
    f.seek(0)
    print(parttwo(f))
