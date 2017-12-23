def short_dance(programs, changes_list):
    programs = [x for x, y in sorted(zip(programs, changes_list),
                                     key=lambda j:j[1])]
    return programs


def dance(programs_dancers):
    programs = programs_dancers[:]
    for move in moves:
        command = move[0]
        if command == 's':
            amount = move[1:]
            first_slice = programs[:-int(amount)]
            second_slice = programs[-int(amount):]
            second_slice.extend(first_slice)
            programs = second_slice
        if command == 'x':
            pos1, pos2 = move[1:].split('/')
            pos1, pos2 = int(pos1), int(pos2)
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
        if command == 'p':
            name1, name2 = move[1:].split('/')
            pos1 = [i for i, x in enumerate(programs) if x == name1][0]
            pos2 = [i for i, x in enumerate(programs) if x == name2][0]
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
    return programs

if __name__ == '__main__':
    with open('day16.txt') as file:
        moves = file.readline().split(',')
    dancers_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p']
    dancers_first_dance = dance(dancers_start)
    print("".join(dancers_first_dance), 'zad1')
    # end of part one

    changes = []
    for index1, mov1 in enumerate(dancers_start):
        index2 = [index2 for index2, mov2 in enumerate(dancers_first_dance) if
                  mov2 == mov1][0]
        changes.append(index2)

    dancers_looping = dancers_start[:]
    nwd = 1000000000
    for i in range(1, 1000000000):
        dancers_looping = dance(dancers_looping)
        if dancers_looping == dancers_start:
            print('nwd:', i)
            nwd = i
            break

    for i in range(1000000000 % nwd):
        dancers_looping = dance(dancers_looping)
        print("".join(dancers_looping), nwd, i)
