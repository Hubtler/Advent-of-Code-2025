from aocAuto import AOC_Auto

aoca = AOC_Auto(day=8, year = 2025, skip_example_part_a=True)

def parse(text):
    lines = text.split("\n")
    positions = [tuple(map(int, line.split(","))) for line in lines]
    return positions

def l2_norm(p1, p2):
    return sum([(x-y)**2 for x,y in zip(p1,p2)])


def part1(input, number_connections = 1000):
    positions = parse(input)
    pairwise_distance = [(l2_norm(p1, p2), i, j) for i, p1 in enumerate(positions) for j, p2 in enumerate(positions[:i])]
    sorted_pairs = sorted(pairwise_distance, key = lambda pair: pair[0])
    connections = [(i,j) for _, i, j in sorted_pairs[:number_connections]]
    id_to_members = {}
    member_with_id = []
    def give_connected_component_id(ind, cid):
        if ind in member_with_id:   # to circumvent circle-connections
            return
        if cid not in id_to_members:
            id_to_members[cid] = []
        id_to_members[cid].append( ind )
        member_with_id.append(ind)
        for i,j in connections:
            if i == ind:
                give_connected_component_id(j, cid)
            if j == ind:
                give_connected_component_id(i, cid)

    current_id = 0
    for i, _ in connections: # only go through the values which have a connection to find biggest connected components
        if i not in id_to_members.values():
            give_connected_component_id(i, current_id)
            current_id += 1

    sizes_of_circuits = sorted( [len(circuit) for circuit in id_to_members.values()], reverse=True ) # descending
    return sizes_of_circuits[0]*sizes_of_circuits[1]*sizes_of_circuits[2]


def part2(input):
    positions = parse(input)
    pairwise_distance = [(l2_norm(p1, p2), i, j) for i, p1 in enumerate(positions) for j, p2 in
                         enumerate(positions[:i])]
    sorted_pairs = sorted(pairwise_distance, key=lambda pair: pair[0])

    def are_all_connected(number_connections):
        member_with_id = []
        connections = [(i, j) for _, i, j in sorted_pairs[:number_connections]]
        def give_connected_component_id(ind):
            if ind in member_with_id:  # to circumvent circle-connections
                return
            member_with_id.append(ind)
            for i, j in connections:
                if i == ind:
                    give_connected_component_id(j)
                if j == ind:
                    give_connected_component_id(i)

        give_connected_component_id(0)
        return len(member_with_id) == len(positions)

    # bisection to find perfect index
    smaller, bigger = len(positions)-1, len(sorted_pairs)   # i need at least len(positions)-1 connections and at most all
    while smaller < bigger-1:
        new_test_value = (smaller + bigger)//2
        if are_all_connected(new_test_value):
            bigger = new_test_value
        else:
            smaller = new_test_value

    last_needed_pair_ind = bigger - 1    # since we need {bigger} number of connections
    _, i, j = sorted_pairs[last_needed_pair_ind]    # obtain position indices of last added connection
    return positions[i][0] * positions[j][0]    # result is the product of the X-coordinates

aoca.auto_submit(part1, part2)