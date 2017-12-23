# from sympy import *
import sys

# def get_min_gradient(grads):
#     min_t = sys.maxsize
#     min_grad = None
#     for i, g in enumerate(grads):
#         grad = str(g).split()
#         if len(grad) == 1 and grad[0].isdigit():
#             if int(grad[0]) < min_t:
#                 min_t = int(grad[0])
#                 min_grad = i
#     return min_grad

if __name__ == '__main__':
    with open('day20.txt') as file:
        particles = file.readlines()
    pts = dict()
    for i, p in enumerate(particles):
        pts[i] = [x[3:].split(',') for x in p.rstrip('\n')[:-1].split('>, ')]
        pts[i] = [[int(z) for z in x] for x in pts[i]]

    # x = Symbol('x')
    # y = Symbol('y')
    # z = Symbol('z')
    # gradients = []
    # for i, p in pts.items():
    #     vx = abs(p[1][0]) * x + (abs(p[2][0]) * x ** 2) / 2
    #     vy = abs(p[1][1]) * y + (abs(p[2][1]) * y ** 2) / 2
    #     vz = abs(p[1][2]) * z + (abs(p[2][2]) * z ** 2) / 2
    #     gradient = vx.diff(x) + vy.diff(x) + vz.diff(x)
    #     gradients.append(gradient)

    all_collisions = set()
    flag = True
    counter = 0
    while flag:
        counter += 1
        print(counter, len(all_collisions))
        flag = False
        # ruch kazdego particla
        for i in range(len(pts.keys())):
            if i not in all_collisions:
                pts[i][1] = [x + y for x, y in zip(pts[i][1], pts[i][2])]
                pts[i][0] = [x + y for x, y in zip(pts[i][0], pts[i][1])]

        # detekcja kolizji
        collisions = set()
        for i in range(len(pts.keys())):
            for j in range(i, len(pts.keys())):
                if i not in all_collisions and j not in all_collisions\
                        and i != j:
                    if pts[i][0] == pts[j][0]:
                        collisions.add(i)
                        collisions.add(j)
                        flag = True
        all_collisions.update(collisions)
        # sprawdzenie warunku
        if not flag:
            collisions = set()
            for i in range(len(pts.keys())):
                for j in range(i, len(pts.keys())):
                    if i not in all_collisions and j not in all_collisions\
                            and i != j:
                        begA, begB = pts[i][0], pts[j][0]
                        dirA, dirB = pts[i][1], pts[j][1]
                        d1 = begA[1] - begB[1]
                        d2 = begB[2] - begA[2]
                        det = dirB[1] * dirA[2] - dirA[1] * dirB[2]
                        if det != 0:
                            u = (dirB[2] * d1 + dirB[1] * d2) / det
                            v = (dirA[2] * d1 + dirA[1] * d2) / det
                            if u > 0 and v > 0:
                                flag = True

    print(len(all_collisions))




