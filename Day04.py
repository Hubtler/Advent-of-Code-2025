from aocAuto import AOC_Auto

aoca = AOC_Auto(day=4, year=2025, skip_example_part_a = True)

class Paper_Role:
    def __init__(self, i, j):
        self.pos = (i, j)
        self.neighbours = []
        self.is_valid = True
    def is_removable(self):
        return len(self.neighbours) < 4
    def remove(self, counter_fun = None):
        if not self.is_valid:
            return
        self.is_valid = False   # to prevent from being removed twice
        if not counter_fun is None:
            counter_fun()
        for neighbour in self.neighbours:
            if self in neighbour.neighbours:
                neighbour.neighbours.remove(self)
        for neighbour in self.neighbours:
            if neighbour.is_removable():
                neighbour.remove(counter_fun)

def parse(text):
    neighbours = [(di, dj) for di in range(-1, 2) for dj in range(-1, 2) if di != 0 or dj != 0]
    lines = text.split("\n")
    paper_roles = {}
    for i0, line in enumerate(lines):
        for j0, c in enumerate(line):
            if c == "@":
                paper_roles[(i0,j0)] = Paper_Role(i0, j0)

    for paper_role in paper_roles.values():
        i0, j0 = paper_role.pos
        for di, dj in neighbours:
            i, j = i0 + di, j0 + dj
            if (i,j) in paper_roles:
                paper_role.neighbours.append( paper_roles[(i,j)] )
    return paper_roles

def part1(input):
    removed_paper_roles = 0
    paper_roles = parse(input)
    for paper_role in paper_roles.values():
        if paper_role.is_removable():
            removed_paper_roles += 1
    return removed_paper_roles


def part2(input):
    paper_roles = parse(input)
    number_removed = 0
    def counter_fun():
        nonlocal number_removed
        number_removed += 1

    for paper_role in paper_roles.values():
        if paper_role.is_removable():
            paper_role.remove(counter_fun)
    return number_removed

aoca.auto_submit(part1, part2)
