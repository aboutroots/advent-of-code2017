from math import ceil, sqrt
from itertools import chain
import numpy as np
import collections


def count_hashes(x):
    counter = 0
    for i in x:
        if i == '#':
            counter += 1
    return counter


def flip_right(rect):
    new_rect = []
    row_len = int(sqrt(len(rect)))
    for i in range(0, len(rect), row_len):
        new_rect.append(rect[i:i + row_len])
    new_rect = list(zip(*new_rect[::-1]))
    r = []
    for x in new_rect:
        r.extend(x)
    return r


def symmetry(rect):
    row_len = int(sqrt(len(rect)))
    new_rect = []
    for i in range(row_len):
        new_rect.extend(list(reversed(rect[i*row_len: i*row_len + row_len])))
    return new_rect


def check_rule(rec, r):
    rul = list(r)
    for i in range(2):
        for j in range(4):
            if rec == rul:
                return True
            rec = flip_right(rec)
        rec = symmetry(rec)
    return False


def build_new(squares, small_rect_size):
    old = list(chain.from_iterable(list(squares.values())))
    # for y in range(int(sqrt(len(old)))):
    #     for x in range(int(sqrt(len(old)))):
    #         print(old[y * int(sqrt(len(old))) + x], end=' ')
    #     print()
    # print(small_rect_size)

    def to_numbers(x):
        if x == '#':
            return 1
        return 0

    def to_chars(x):
        if x == 1:
            return '#'
        return '.'

    def rect_generator(array, length):
        rects = np.split(array, len(array) // length)
        for i in range(len(rects)):
            yield rects[i]

    old = [to_numbers(x) for x in old]
    old = np.array(old)

    size = len(old)
    # print(size)
    # old = old.reshape(int(sqrt(size)), int(sqrt(size)))
    new = np.zeros((int(sqrt(size)), int(sqrt(size))))

    side = int(sqrt(small_rect_size))
    small_rect = rect_generator(old, small_rect_size)
    for row in range(0, int(sqrt(size)), side):
        for col in range(0, int(sqrt(size)), side):
            new[row:row + side, col:col + side] = next(small_rect).reshape(
                side, side)


    return [to_chars(int(x)) for x in new.flatten()]


def solve():
    rect = ['.', '#', '.',
            '.', '.', '#',
            '#', '#', '#']
    for iteration in range(18):
        if not len(rect) % 2:
            squares = collections.OrderedDict()
            cells_in_row = int(sqrt(len(rect)))
            for y in range(cells_in_row):
                for x in range(cells_in_row):
                    if (y // 2, x // 2) in squares:
                        squares[(y // 2, x // 2)].append(
                            rect[x + cells_in_row * y])
                    else:
                        squares[(y // 2, x // 2)] = [
                            rect[x + cells_in_row * y]]
        else:
            squares = collections.OrderedDict()
            l = len(rect)
            cells_in_row = int(sqrt(len(rect)))
            for y in range(cells_in_row):
                for x in range(cells_in_row):
                    if (y//3, x//3) in squares:
                        squares[(y//3, x//3)].append(rect[x+cells_in_row*y])
                    else:
                        squares[(y // 3, x // 3)] = [rect[x+cells_in_row*y]]

        small_rect_size = 0
        for i, square in sorted(squares.items()):
            # find matching rule
            small_rect_size = (sqrt(len(square))+1)**2
            for rule, new_rect in rules.items():
                if len(square) is len(rule):
                    if count_hashes(square) == count_hashes(rule):
                        if check_rule(square, rule):
                            squares[i] = new_rect
                            break

        # build new rect from squares
        # print(squares)
        if iteration > 0:
            rect = build_new(squares, small_rect_size)
        else:
            rect = list(chain.from_iterable(list(squares.values())))
        # for y in range(int(sqrt(len(rect)))):
        #     for x in range(int(sqrt(len(rect)))):
        #         print(rect[y*int(sqrt(len(rect)))+x], end=' ')
        #     print()
        # print()
    print(count_hashes(rect))

if __name__ == '__main__':
    with open('day21.txt') as file:
        lines = [line.rstrip('\n').split(' => ') for line in file.readlines()]
    rules = dict()
    for rule in lines:
        first = tuple([x for x in rule[0] if x != '/'])
        second = [x for x in rule[1] if x != '/']
        rules[first] = second
    solve()
