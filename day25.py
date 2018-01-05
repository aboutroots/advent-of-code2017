ones = set()
pos = 0
state = 'A'
for i in range(12629077):
    if state == 'A':
        if pos not in ones:
            ones.add(pos)
            pos += 1
            state = 'B'
        else:
            if pos in ones:
                ones.remove(pos)
            pos -= 1
            state = 'B'

    elif state == 'B':
        if pos not in ones:
            if pos in ones:
                ones.remove(pos)
            pos += 1
            state = 'C'
        else:
            ones.add(pos)
            pos -= 1
            state = 'B'

    elif state == 'C':
        if pos not in ones:
            ones.add(pos)
            pos += 1
            state = 'D'
        else:
            if pos in ones:
                ones.remove(pos)
            pos -= 1
            state = 'A'

    elif state == 'D':
        if pos not in ones:
            ones.add(pos)
            pos -= 1
            state = 'E'
        else:
            ones.add(pos)
            pos -= 1
            state = 'F'

    elif state == 'E':
        if pos not in ones:
            ones.add(pos)
            pos -= 1
            state = 'A'
        else:
            if pos in ones:
                ones.remove(pos)
            pos -= 1
            state = 'D'

    elif state == 'F':
        if pos not in ones:
            ones.add(pos)
            pos += 1
            state = 'A'
        else:
            ones.add(pos)
            pos -= 1
            state = 'E'

    # print('{} :::'.format(i),end='')
    # for j in range(-7, 7):
    #     if pos == j:
    #         print('[',end='')
    #     else:
    #         print(' ', end='')
    #
    #     if j in ones:
    #         print('1', end='')
    #     else:
    #         print('0', end='')
    #
    #     if pos == j:
    #         print(']',end='')
    #     else:
    #         print(' ', end='')
    # print()
print(len(ones))