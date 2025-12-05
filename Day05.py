from aocAuto import AOC_Auto

aoca = AOC_Auto(day=5, year=2025)

def parse(text):
    text_parts = text.split("\n\n")
    first_lines = text_parts[0].split("\n")
    fresh_ingredient_ranges = [tuple(map(lambda x: int(x), line.split("-"))) for line in first_lines]
    second_lines = text_parts[1].split("\n")
    ingredient_ids = [int(id_str) for id_str in second_lines]
    return fresh_ingredient_ranges, ingredient_ids

def part1(input):
    fresh_ingredient_ranges, ingredient_ids = parse(input)
    sum_available_fresh_ingredients = 0
    for id in ingredient_ids:
        for id_range_lower, id_range_upper in fresh_ingredient_ranges:
            if id_range_lower <= id <= id_range_upper:
                sum_available_fresh_ingredients += 1
                break
    return sum_available_fresh_ingredients

def part2(input):
    fresh_ingredient_ranges, _ = parse(input)
    # to avoid double counting, make them disjoint
    # first, sort them by left range
    fresh_ingredient_ranges = sorted(fresh_ingredient_ranges, key = lambda r: r[0])
    # second, union two neighboring intervals if they intersect
    reduced_ranges = []
    i = 0
    while i < len(fresh_ingredient_ranges):
        actual_lower_bound, actual_upper_bound = fresh_ingredient_ranges[i]
        next_i = i + 1
        for j, (id_range_lower, id_range_upper) in enumerate(fresh_ingredient_ranges[i+1:]):
            if id_range_lower <= actual_upper_bound: # since they are sorted, they have an intersection
                actual_upper_bound = max(actual_upper_bound, id_range_upper)
                next_i = i + 1 + j + 1 # such if j = 0 we start at i + 2 (one after j=0 which corresponds to i+1) with the next intersection test
            else:   # otherwise, no further interval will have an intersection
                break
        i = next_i
        reduced_ranges.append( (actual_lower_bound, actual_upper_bound) )
    total_fresh_ingredients = 0
    for id_range_lower, id_range_upper in reduced_ranges:
        total_fresh_ingredients += id_range_upper - id_range_lower + 1
    return total_fresh_ingredients

aoca.auto_submit(part1, part2)