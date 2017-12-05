
def count_valid(filename):
    valid = 0
    with open(filename) as f:
        rows = f.readlines()
        for row in rows:
            elements = list(row.rstrip().split(' '))
            different = set(elements)
            if len(different) is len(elements):
                valid += 1

    return valid


def count_valid2(filename):
    valid = 0
    with open(filename) as f:
        rows = f.readlines()
        for row in rows:
            elements = list(row.rstrip().split(' '))
            different = set(elements)
            if len(different) is len(elements):
                flag = True
                for i in range(len(elements)):
                    if not flag:
                        break
                    for j in range(i + 1, len(elements)):
                        if not flag:
                            break
                        if set(elements[i]) == set(elements[j]):
                            flag = False
                if flag:
                    valid += 1


    return valid

if __name__ == "__main__":
    print(count_valid2('day4.txt'))