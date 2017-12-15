layers = [l.rstrip('\n') for l in open('day13.txt').readlines()]
layers = dict([(int(l.split(': ')[0]), int(l.split(': ')[1])) for
               l in layers])
severity = 0
for t in range(max(layers.keys())):
    if t in layers.keys() and not t % (2 * (layers[t] - 1)):
        severity += t * layers[t]
print(severity)
delay = 0
go = False

while not go:
    delay += 1
    go = True
    for t in layers.keys():
        if not (t + delay) % (2 * (layers[t] - 1)):
            go = False
            break

print(delay)