import math
from itertools import cycle


def steps(square):
    sqr = math.sqrt(square)
    circle_num = sqr/2
    dec = circle_num - math.floor(circle_num)
    if dec <= 0.5:
        circle_num = math.floor(circle_num)
    else:
        circle_num = math.ceil(circle_num)

    # get control points of given circle
    lower_exp = math.floor(sqr)
    if not lower_exp % 2:
        lower_exp -= 1
    if sqr - lower_exp == 0:
        lower_exp -= 2

    p1 = lower_exp ** 2 + circle_num
    p2 = p1 + 2*circle_num
    p3 = p2 + 2 * circle_num
    p4 = p3 + 2 * circle_num

    distances = [abs(x - square) for x in [p1, p2, p3, p4]]
    dist_1 = min(distances)

    return dist_1 + circle_num


def first_bigger(square):
    puzzles = dict()
    # initialization of first 10 puzzles
    puzzles[(0, 0)] = 1
    puzzles[(1, 0)] = 1
    puzzles[(1, 1)] = 2
    puzzles[(0, 1)] = 4
    puzzles[(-1, 1)] = 5
    puzzles[(-1, 0)] = 10
    puzzles[(-1, -1)] = 11
    puzzles[(0, -1)] = 23
    puzzles[(1, -1)] = 25
    puzzles[(2, -1)] = 26

    # go up and check left, go left and check down.. etc.
    directions = [((0, 1), (-1, 0)), ((-1, 0), (0, -1)), ((0, -1), (1, 0)),
                  ((1, 0), (0, 1))]

    # all puzzles nearby
    neighbours = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1),
                  (1, 0), (1, 1)]

    moves = cycle(directions)
    move = next(moves)

    ptr = [2, -1, 26]   # our actual puzzle
    while True:
        if (ptr[0] + move[1][0], ptr[1] + move[1][1]) in puzzles.keys():
            # go straight
            ptr[0] += move[0][0]
            ptr[1] += move[0][1]
        else:
            # turn and change movement
            ptr[0] += move[1][0]
            ptr[1] += move[1][1]
            move = next(moves)

        ptr[2] = 0
        # calculate puzzle value
        for n in neighbours:
            if (ptr[0] + n[0], ptr[1] + n[1]) in puzzles.keys():
                ptr[2] += puzzles[(ptr[0] + n[0], ptr[1] + n[1])]
        if ptr[2] > square:
            return ptr[2]
        print(ptr[2])

        # save value
        puzzles[(ptr[0], ptr[1])] = ptr[2]

if __name__ == "__main__":
    print(first_bigger(361527))

