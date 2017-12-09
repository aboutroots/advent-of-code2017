def group_value(filename):
    with open(filename) as f:
        data = f.readlines()[0]
    flag_garbage = False
    flag_skip = 0
    counter, value, garbage = 1, 0, 0

    for x in data:
        garbage_opening = False
        if x == '!' and not flag_skip:
            flag_skip = 2
        if not flag_skip:
            if x == '<':
                if not flag_garbage:
                    flag_garbage = True
                    garbage_opening = True
            if x == '>':
                flag_garbage = False
            if not flag_garbage:
                if x == '{':
                    value += counter
                    counter += 1
                if x == '}':
                    counter -= 1
            if flag_garbage:
                if not garbage_opening:
                    garbage += 1

        if flag_skip:
            flag_skip -= 1

    return value, garbage

if __name__ == "__main__":
    print(group_value('day9.txt'))
