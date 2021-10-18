with open("input.txt") as f:
    lines = f.readlines()


def check_weight(tower, name):
    children = tower[name]["children"]
    totals = [tower[c]["total"] for c in children]
    if len(set(totals)) == 1:
        return name, tower[name]
    for k in range(len(totals)):
        mupp = len(set(totals[:k] + totals[k+1:]))
        if mupp == 1:
            return check_weight(tower, tower[name]["children"][k])
        elif mupp == 0:
            raise Exception("Nä?!")



def update_total_weight(tower, name):
    upd = lambda x : update_total_weight(tower, x)
    tower[name]["total"] = sum(map(upd, tower[name]["children"])) + tower[name]["weight"]
    return tower[name]["total"]




ap = {}
for line in lines:
    s = line.split(" -> ")
    s0 = s[0].split(' ')
    name = s0[0]
    weight = int(s0[1].strip("()  \n"))
    ap[name] = {"is_child": False}
    ap[name]['weight'] = weight
    try:
        cpre = s[1].split(',')
        ap[name]['children'] = list(map(lambda cs : cs.strip(), cpre))
    except:
        ap[name]['children'] = list()

for grej in ap:
    for child in ap[grej]["children"]:
        ap[child]["is_child"] = True

bottoms = set()
for grej in ap:
    if not(ap[grej]["is_child"]):
        bottoms.add(grej)

print(ap)

for bottom in bottoms:
    update_total_weight(ap, bottom)
    print(bottom)
    cw = check_weight(ap, bottom)
    

