from aocAuto import AOC_Auto

aoca = AOC_Auto(day=9, year = 2025, skip_example_part_a=True)

def parse(text):
    lines = text.split("\n")
    coordinates = [tuple(map(int, line.split(","))) for line in lines]
    return coordinates


def part1(input):
    coordinates = parse(input)
    areas = [(abs(x1-x0)+1)*(abs(y1-y0)+1) for ind,(x0,y0) in enumerate(coordinates) for x1,y1 in coordinates[(ind+1):]]
    return max(areas)


def lines_crosses(l1, l2):
    "checks if l1 intersects with l2. Touching is not enough, l2 should really cut l1 into 2 parts"
    x1_from, y1_from, x1_to, y1_to = l1
    x2_from, y2_from, x2_to, y2_to = l2

    l1_vertical = (x1_from == x1_to)
    l2_vertical = (x2_from == x2_to)
    if l1_vertical == l2_vertical:
        return False

    # one is horizontal, one vertical. Ensure l1 is vertical
    if not l1_vertical:
        x2_from, y2_from, x2_to, y2_to = l1 # horizontal (i.e. x2_from != x2_to and y2_from == y2_to)
        x1_from, y1_from, x1_to, y1_to = l2 # vertical (i.e. y1_from != y1_to and x1_from == x1_to)

    # normalize ranges
    y1_from, y1_to = sorted((y1_from, y1_to))
    x2_from, x2_to = sorted((x2_from, x2_to))

    return (x2_from < x1_from < x2_to) and (y1_from < y2_from < y1_to)

def is_inside(x, y, coordinates):
    """ check if (x,y) is inside the path of the polygonal path given by coordinates
    coordinates: list of (x, y) vertices; successive vertices share x or y."""
    n = len(coordinates)
    inside = False
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[( i + 1 ) % n]

        # Boundary Check
        if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
            return True

        # Ray casting: count crossings of ray to the right from (x, y)
        # Only vertical segments can be crossed by a horizontal ray
        if x1 == x2:
            if ( (y1 > y) != (y2 > y) ) and x < x1:
                inside = not inside

    return inside

def is_valid_rectangle(p1, p2, coordinates):
    x1, y1 = p1
    x2, y2 = p2
    n = len(coordinates)
    corners = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
    for x, y in corners:
        if not is_inside(x, y, coordinates):
            return False
    for ind in range(4):
        for ind2 in range(n):
            if lines_crosses((*corners[ind], *corners[(ind+1)%4]), (*coordinates[ind2], *coordinates[(ind2 + 1) % n])):
                return False
    return True

def part2(input):
    coordinates = parse(input)
    areas = [(abs(x1-x0)+1)*(abs(y1-y0)+1) for ind,(x0,y0) in enumerate(coordinates) for x1,y1 in coordinates[(ind+1):] if is_valid_rectangle((x0,y0), (x1, y1), coordinates ) ]
    return max(areas)

aoca.auto_submit(part1, part2)