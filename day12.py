def groups(number, vertice):
    if vertice not in used_vertices:
        used_vertices.add(vertice)
        villages[number].append(vertice)
        for c in graph[vertice]:
            groups(number, c)

if __name__ == '__main__':
    with open('day12.txt') as file:

        lines = [line.rstrip('\n').split(' <-> ') for line in file.readlines()]
        lines = [(line[0], [l.rstrip(',') for l in line[1].split()]) for line in
                 lines]
        graph = dict(lines)
        villages = dict()
        used_vertices = set()
        for num, v in enumerate(graph.keys()):
            villages[num] = []
            groups(num, v)
            if len(used_vertices) == len(graph.keys()):
                break

        villages = {k: v for k, v in villages.items() if len(v) > 0}
        for verts in villages.values():
            if '0' in verts:
                print(len(verts))
        print(len(villages.keys()))

