def root_name(filename, weights, children):
    with open(filename) as f:
        programs = [x.rstrip('\n') for x in f.readlines()]
        for program in programs:
            spl = program.split(' -> ')
            name, weight = spl[0].split(' (')
            weight = int(weight.rstrip(')'))
            sequence = None
            try:
                sequence = [x.rstrip(',') for x in spl[1].split()]
            except IndexError:
                pass

            children[name] = sequence

    for name in children.keys():
        found = True
        for all_children in children.values():
            if not found:
                break
            if all_children:
                for child in all_children:
                    if child == name:
                        found = False
                        break
        if found:
            return name


def get_repaired_weight(name):
    weight = weights[name]

    weight_of_every_tower = None
    last_child = None
    if children[name]:
        for index, child in enumerate(children[name]):
            child_weight = get_repaired_weight(child)
            if index == 0:
                weight_of_every_tower = child_weight
            if child_weight != weight_of_every_tower:
                difference = child_weight - weight_of_every_tower
                result = weights[child] - difference
                raise Exception(result)
            weight += child_weight
            last_child = child

    return weight


def balance(filename):
    with open(filename) as f:
        programs = [x.rstrip('\n') for x in f.readlines()]
        for program in programs:
            spl = program.split(' -> ')
            name, weight = spl[0].split(' (')
            weight = int(weight.rstrip(')'))
            sequence = None
            try:
                sequence = [x.rstrip(',') for x in spl[1].split()]
            except IndexError:
                pass

            weights[name] = weight
            children[name] = sequence

    root = None
    for name in children.keys():
        found = True
        for all_children in children.values():
            if not found:
                break
            if all_children:
                for child in all_children:
                    if child == name:
                        found = False
                        break
        if found:
            root = name
    try:
        get_repaired_weight(root)
    except Exception as e:
        return e

if __name__ == "__main__":
    weights = dict()
    children = dict()
    print(balance('day7.txt'))

