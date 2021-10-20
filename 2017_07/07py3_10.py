def read_line(line):
    match line.split():
        case [name, weight]:
            return {'name': name, 'weight': weight, 'subtowers': []}
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
            tower['is_root' = True]
            tower_dict[tower['name']: tower]
    for name in tower_dict:
        for subname in tower_dict[name]['subtowers']:
            tower_dict[name]['is_root'] = False
    return tower_dict

