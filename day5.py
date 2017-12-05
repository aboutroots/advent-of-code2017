def escape(filename):
    counter = 0
    with open(filename) as f:
        steps = [int(x.rstrip('\n')) for x in list(f.readlines())]

    ptr = 0
    while True:
        try:
            old = ptr
            ptr = ptr + steps[ptr]
            steps[old] += 1
            counter += 1
        except IndexError as exc:
            break
    return counter

def escape2(filename):
    counter = 0
    with open(filename) as f:
        steps = [int(x.rstrip('\n')) for x in list(f.readlines())]

    ptr = 0
    while True:
        try:
            old = ptr
            ptr = ptr + steps[ptr]
            if steps[old] >= 3:
                steps[old] -= 1
            else:
                steps[old] += 1
            counter += 1
        except IndexError as exc:
            break
    return counter

if __name__ == "__main__":
    print(escape2('day5.txt'))