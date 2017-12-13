steps = open('day11.txt').readline().replace(',', ', ') + ','
dic, pos, dist = {'sw,': 'x.-1', 'se,': 'y.-1', 's,': 'z.1', 'nw,': 'y.1',
                  'ne,': 'x.1',  'n,': 'z.-1'}, {'x': 0, 'y': 0, 'z': 0}, []
for i, j in dic.items():
    steps = steps.replace(i, j)
for step in steps.split(' '):
    pos[step.split('.')[0]] += int(step.split('.')[1])
    x = sorted(pos.values(), key=lambda i: abs(i), reverse=True)
    dist.append(abs(x[0]) + abs(x[1]))
print(dist[-1], max(dist))

