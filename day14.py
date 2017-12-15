from day10 import knot_hash
from PIL import Image
from random import randrange


if __name__ == '__main__':
    rows, used = [], 0
    [rows.append(knot_hash('wenycdww'+'-'+str(i))) for i in range(128)]
    bits_grid = []
    for row in rows:
        bits_array = [str(format(int(b, 16), '04b')) for b in row]
        bits_grid.append("".join(bits_array))
        used += "".join(bits_array).count('1')
    print('zad1', used)

    # zadanie 2
    number = 0
    regions = dict()
    queue = list()
    nbrs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for i in range(128):
        for j in range(128):
            is_one = bits_grid[i][j] == '1'
            not_used_before = (i, j) not in [x for v in regions.values() for x in v]
            if is_one and not_used_before:
                if number not in regions.keys():
                    regions[number] = list()

                regions[number].append((i, j))
                queue.insert(0, (i, j))
                # looking for neighbours
                while len(queue):
                    element = queue.pop()
                    for nbr in [(element[0]+x, element[1]+y) for x, y in nbrs]:
                        # ugly booleans for neighbours
                        if 0 <= nbr[0] < 128 and 0 <= nbr[1] < 128 and\
                        nbr not in [x for v in regions.values() for x in v]\
                        and bits_grid[nbr[0]][nbr[1]] == '1':

                                regions[number].append(nbr)
                                queue.insert(0, nbr)
                number += 1

    print('zad2', len(regions.keys()))

    list_of_pixels = bits_grid
    img = Image.new('RGB', (128, 128), "black")
    pixels = img.load()
    colors = dict()
    for g in regions.keys():
        colors[g] = (randrange(0, 255), randrange(0, 255),
                     randrange(0, 255), 255)
    for k, v in regions.items():
        for pixel in v:
            pixels[pixel] = colors[k]

    img.show()