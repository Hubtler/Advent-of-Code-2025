from collections import defaultdict

from aocAuto import AOC_Auto

aoca = AOC_Auto(day=8, year = 2025, skip_example_part_a=True)

def parse(text):
    lines = text.split("\n")
    positions = [tuple(map(int, line.split(","))) for line in lines]
    return positions

def l2_norm(p1, p2):
    return sum([(x-y)**2 for x,y in zip(p1,p2)])

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.num_sets = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] <= self.rank[y_root]:
            self.parent[x_root] = y_root
            self.rank[y_root] += self.rank[x_root]
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += self.rank[y_root]

        self.num_sets -= 1
        return True


def part1(input, number_connections = 1000):
    positions = parse(input)
    pairwise_distance = [(l2_norm(p1, p2), i, j) for i, p1 in enumerate(positions) for j, p2 in enumerate(positions[:i])]
    sorted_pairs = sorted(pairwise_distance, key = lambda pair: pair[0])
    connections = [(i,j) for _, i, j in sorted_pairs[:number_connections]]
    uf = UnionFind( len(positions) )
    for i, j in connections:
        uf.union(i, j)

    root_members = defaultdict(int) # dict with initial value 0
    for i in range(len(positions)):
        root_members[ uf.find(i) ] += 1

    sizes_of_circuits = sorted( root_members.values(), reverse=True ) # descending
    return sizes_of_circuits[0]*sizes_of_circuits[1]*sizes_of_circuits[2]


def part2(input):
    positions = parse(input)
    pairwise_distance = [(l2_norm(p1, p2), i, j) for i, p1 in enumerate(positions) for j, p2 in enumerate(positions[:i])]
    sorted_pairs = sorted(pairwise_distance, key=lambda pair: pair[0])
    uf = UnionFind( len(positions) )
    number_of_edges = 0
    i, j = 0, 0
    while number_of_edges < len(positions)-1:   # to connect N Points, N-1 edges are needed
        _, i, j = sorted_pairs.pop(0)
        if uf.union(i,j):
            number_of_edges += 1

    return positions[i][0] * positions[j][0]    # result is the product of the X-coordinates

aoca.auto_submit(part1, part2)