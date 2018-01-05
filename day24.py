import numpy as np

with open('day24.txt') as file:
    bricks = [tuple(x.rstrip('\n').split('/')) for x in \
            file.readlines()]
print(bricks)

bridges = set()
# base bricks
for brick in bricks:
    if brick[0] == '0':
        bridges.add(brick)
    if brick[1] == '0':
        bridges.add(tuple(reversed(brick)))

new_flag = True
while new_flag:
    print(len(list(bridges)[-1]))

    new_flag = False
    new_bridges = set()
    old_bridges = set()
    for bridge in bridges:
        no_more_bricks = True
        for brick in bricks:    # try to fit a brick
            if brick not in bridge and tuple(reversed(brick)) not in bridge \
                    and brick != bridge and tuple(reversed(brick)) != bridge:
                last_port = bridge[-1]
                if len(bridge[-1]) > 1:
                    last_port = last_port[-1]

                if last_port == brick[0]:
                    new_bridge = list(bridge)
                    if len(bridge[-1]) == 1:
                        new_bridge = [bridge]
                    new_bridge.append(brick)
                    new_flag = True
                    no_more_bricks = False
                    new_bridges.add(tuple(new_bridge))
                    old_bridges.add(bridge)

                if last_port == brick[1]:
                    new_bridge = list(bridge)
                    if len(bridge[-1]) == 1:
                        new_bridge = [bridge]
                    new_bridge.append(tuple(reversed(brick)))
                    new_flag = True
                    no_more_bricks = False
                    new_bridges.add(tuple(new_bridge))
                    old_bridges.add(bridge)

        if no_more_bricks:
            old_bridges.add(bridge)
        if len(bridge) == 35:
                print(sum([int(x) for x in np.array(bridge).flatten()]))

    bridges.update(new_bridges)
    print(max(sum([int(x) for x in np.array(b).flatten()]) for b in bridges))
    bridges = bridges.difference(old_bridges)

