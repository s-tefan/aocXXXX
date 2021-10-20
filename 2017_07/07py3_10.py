def read_line(line):
    match line.split():
        case [name, weight]:
            return {'name': name, 'weight': eval(weight), 'subtowers': []}
        case [name, weight, "->", *subtowers]:
            return {'name': name, 'weight': weight, 'subtowers': subtowers}
        case _:
            raise Exception("Blö!")

def read_file(file_name):
    tower_dict = {}  
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            tower = read_line(line)
            tower['is_root'] = True
            tower_dict[tower['name']] = tower
    for name in tower_dict:
        for subname in tower_dict[name]['subtowers']:
            tower_dict[name]['is_root'] = False
    return tower_dict

td = read_file('input.txt')
roots = filter(lambda x : td[x]['is_root'], td)
print(*roots)
print()
for name in td:
    if td[name]['is_root']:
        print(td[name])

