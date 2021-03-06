import json


class Red(Exception):
    pass


def sumof(obj):
    try:
        return 0 + obj  # works for numbers (and booleans)
    except:
        if len(obj):
            try:
                if parttwo and "red" in obj.values():
                    raise Red
                # works on dict (json object)
                return sum(map(sumof, obj.values()))
            except:
                try:
                    return sum(map(sumof, obj))  # works on list (json array)
                except:
                    return 0  # If string (or any illegal element), or Red raised 
        else:
            return 0


def doit(filename):
    with open(filename) as f:
        return sumof(json.load(f))


parttwo = False
print(doit("input.txt"))
parttwo = True
print(doit("input.txt"))
