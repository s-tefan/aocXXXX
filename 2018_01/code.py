
def partone(file):
    return sum(int(r) for r in file)


def parttwo(file):
    fr = 0
    fr_set = set()
    fr_set.add(fr)
    while True:
        file.seek(0)
        for line in file:
            fr += int(line)
            if fr in fr_set:
                return fr
            fr_set.add(fr)


with open('input') as f:
    print(partone(f))
    print(parttwo(f))

