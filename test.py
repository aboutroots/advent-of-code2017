import numpy as np
from math import sqrt

old = ['#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#', '.', '#', '.', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '.', '#', '.', '#', '#', '#', '#', '.', '.', '#', '.']
print(len(old))

def new_rect(old):
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
    # old = old.reshape(int(sqrt(size)), int(sqrt(size)))
    new = np.zeros((int(sqrt(size)), int(sqrt(size))))

    if size % 2 == 0:
        small_rect = rect_generator(old, 4)
        for row in range(0, int(sqrt(size)), 2):
            for col in range(0, int(sqrt(size)), 2):
                new[row:row + 2, col:col + 2] = next(small_rect).reshape(2, 2)

    else:
        small_rect = rect_generator(old, 9)
        for row in range(0, int(sqrt(size)), 3):
            for col in range(0, int(sqrt(size)), 3):
                new[row:row + 3, col:col + 3] = next(small_rect).reshape(3, 3)

    return [to_chars(int(x)) for x in new.flatten()]

print(old)
print(new_rect(old))