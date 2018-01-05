import tqdm

with open("day22.txt") as file:
    virus_map = [list(x.rstrip('\n')) for x in file.readlines()]

pos = [12, 12]
infected = set()
weakened = set()
flagged = set()
initial = set()

for y in range(len(virus_map)):
    for x in range(len(virus_map[y])):
        if virus_map[y][x] == '#':
            node = (y, x)
            infected.add(node)
            initial.add(node)

direction = [-1, 0]  # y, x

counter = 0
for i in tqdm.tqdm(range(10000000)):
    if tuple(pos) in infected:
        # right
        old = list(direction)
        direction[0] = old[1]
        direction[1] = -old[0]
        infected.remove(tuple(pos))
        flagged.add(tuple(pos))
        if tuple(pos) in initial:
            initial.remove(tuple(pos))

    elif tuple(pos) in flagged:
        # reverse
        old = list(direction)
        direction[0] = -old[0]
        direction[1] = -old[1]
        flagged.remove(tuple(pos))

    elif tuple(pos) in weakened:
        weakened.remove(tuple(pos))
        infected.add(tuple(pos))
        if tuple(pos) not in initial:
            counter += 1
    else:
        # left
        old = list(direction)
        direction[0] = -old[1]
        direction[1] = old[0]
        weakened.add(tuple(pos))

    pos[0] += direction[0]
    pos[1] += direction[1]

    # for y in range(-6,6):
    #     for x in range(-6,6):
    #         if [y, x] == pos:
    #             print('[', end='')
    #         else:
    #             print(' ', end='')
    #
    #         if (y, x) in infected:
    #             print('#', end='')
    #         elif (y, x) in weakened:
    #             print('W', end='')
    #         elif (y, x) in flagged:
    #             print('F', end='')
    #         else:
    #             print('.', end='')
    #
    #         if [y, x] == pos:
    #             print(']', end='')
    #         else:
    #             print(' ', end='')
    #     print()
    # print(counter)
print(counter)