
def partone(file):
    twice_count = 0
    thrice_count = 0
    for r in file:
        box_id = r.strip()
        box_dict = dict()
        for c in box_id:
            if c in box_dict:
                box_dict[c] += 1
            else:
                box_dict[c] = 1
        if 2 in box_dict.values():
            twice_count += 1
        if 3 in box_dict.values():
            thrice_count += 1
    return twice_count*thrice_count




def parttwo(file):
    box_ids = [r.strip() for r in file]
    for n, id1 in enumerate(box_ids):
        for id2 in box_ids[n+1:]:
            eq = [id1[k] == id2[k] for k in range(len(id1))]
            if eq.count(False) == 1:
                i = eq.index(False)
                return id1, id2, id1[:i]+id1[i+1:]
    


with open('input.txt') as f:
    print(partone(f))
    f.seek(0)
    print(parttwo(f))

