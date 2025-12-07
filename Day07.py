import functools

from aocAuto import AOC_Auto

aoca = AOC_Auto(day=7, year=2025)

def parse(text):
    lines = text.split("\n")
    laser_position = None
    splitting_positions = []
    map_height = len(lines)
    map_width = len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                splitting_positions.append((i, j))
            elif c == "S":
                laser_position = (i,j)
    return laser_position, splitting_positions, map_height, map_width

def part1(input):
    laser_position, splitting_positions, map_height, map_width = parse(input)

    laser_tips = [laser_position]
    active_laser_positions = {laser_position}
    number_splits = 0
    while laser_tips:
        i,j = laser_tips.pop()
        if i+1 >= map_height:
            continue
        down_pos = (i+1, j)
        if not down_pos in splitting_positions:
            laser_tips.append( down_pos )
            active_laser_positions.add(down_pos)
        if down_pos in splitting_positions:
            beam_split_pos_1 = (i+1, j-1)
            beam_split_pos_2 = (i+1, j+1)
            split = False
            if 0 <= beam_split_pos_1[1] < map_width and beam_split_pos_1 not in active_laser_positions:
                laser_tips.append( beam_split_pos_1 )
                active_laser_positions.add( beam_split_pos_1)
                split = True
            if 0 <= beam_split_pos_2[1] < map_width and beam_split_pos_2 not in active_laser_positions:
                laser_tips.append(beam_split_pos_2)
                active_laser_positions.add(beam_split_pos_2)
                split = True
            if split:
                number_splits += 1
    return number_splits


def part2(input):
    laser_position, splitting_positions, map_height, map_width = parse(input)
    @functools.cache
    def compute_timelines(i0,j0):
        i, j = i0, j0
        while (i+1,j) not in splitting_positions:
            if i + 1 >= map_height:
                return 1    # one timeline ends
            i += 1
        #(i+1,j) is now in splitting_positions
        number_timelines = 0   # own timeline gets destroyed (and up to 2 gets newly created)
        if 0 <= j-1 < map_width:
            number_timelines += compute_timelines(i+1,j-1)
        if 0 <= j+1 < map_width:
            number_timelines += compute_timelines(i+1,j+1)
        return number_timelines

    return compute_timelines(*laser_position)

aoca.auto_submit(part1, part2)