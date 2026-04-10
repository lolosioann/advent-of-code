from math import dist


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:  # same group
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = []
        self.uf = None

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def add_union_find(self):
        self.uf = UnionFind(self.V)

    def kruskal(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])  # sort by edge size

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.uf.find(u)
            y = self.uf.find(v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.uf.union(x, y)

        return result


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # build list of all points
    points = []
    for line in lines:
        coords = list(map(int, line.strip().split(",")))
        points.append(coords)

    # create graph and add the edges to it
    g = Graph(len(points))
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            g.add_edge(i, j, dist(points[i], points[j]))

    g.add_union_find()
    res = g.kruskal()
    box1, box2 = points[res[-1][0]], points[res[-1][1]]
    print(box1[0] * box2[0])


if __name__ == "__main__":
    main()
