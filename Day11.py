from aocAuto import AOC_Auto
import functools

aoca = AOC_Auto(day=11, year=2025, skip_example_part_a=True, skip_example_part_b=True)

def parse(text):
    name_connected = {}
    lines = text.split("\n")
    for line in lines:
        parts = line.split(": ")
        name_connected[parts[0]] = parts[1].split(" ")
    return name_connected

def get_solver(name_connected):
    @functools.cache
    def connections_to_out_through(name, visit_first = tuple()):
        if len(visit_first) == 0:
            if name == "out":
                return 1
        elif name in visit_first:
            visit_first = tuple(n for n in visit_first if n != name)

        if name not in name_connected:
            return 0

        return sum(connections_to_out_through(n, visit_first) for n in name_connected[name])
    return connections_to_out_through

def part1(input):
    name_connected = parse(input)
    connections_to_out = get_solver(name_connected)
    return connections_to_out('you')


def part2(input):
    name_connected = parse(input)
    connections_to_out = get_solver(name_connected)
    return connections_to_out("svr", ("dac", "fft"))

aoca.auto_submit(part1, part2)