with open("input.txt") as f:
    lines = f.readlines()



def total_weight(tower, bottom):
    print(bottom)
    subtowers = tower[bottom]["children"]
    if subtowers == set():
        return tower[bottom]["weight"]
    else:
        subweights = list(map(lambda x : total_weight(tower, x), subtowers))
        if len(set(subweights)) == 1:
            weight = sum(subweights) + tower[bottom]["weight"]
            print(bottom, weight)
            return weight
        else:
            for k in range(len(subweights)):
                # Äsch. Behöver dra igenom deltornen
                bla = subweights[k]
                blu = set(subweights[:k]+subweights[k+1:])
                if len(blu) == 1:
                    corrected_weight = "bluppblupp"
            raise Exception("För Sören! " + bottom + " " + str(corrected_weight))




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
        ap[name]['children'] = set(map(lambda cs : cs.strip(), cpre))
    except:
        ap[name]['children'] = set()

for grej in ap:
    for child in ap[grej]["children"]:
        ap[child]["is_child"] = True

bottoms = set()
for grej in ap:
    if not(ap[grej]["is_child"]):
        bottoms.add(grej)


for bottom in bottoms:
    print(bottom)
    print(total_weight(ap, bottom))

