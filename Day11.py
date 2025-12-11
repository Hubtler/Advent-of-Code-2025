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


def part1(input):
    name_connected = parse(input)
    @functools.cache
    def connections_to_out(name):
        if name == "out":
            return 1
        if name not in name_connected:
            return 0
        return sum(connections_to_out(n) for n in name_connected[name])
    return connections_to_out('you')


def part2(input):
    name_connected = parse(input)
    @functools.cache
    def connections_to_out_dacfft(name, dac_seen=False, fft_seen=False):
        if dac_seen and fft_seen and name == "out":
            return 1
        if name not in name_connected:
            return 0
        if name == "dac":
            dac_seen = True
        if name == "fft":
            fft_seen = True

        return sum(connections_to_out_dacfft(n, dac_seen, fft_seen) for n in name_connected[name])
    return connections_to_out_dacfft('svr')

aoca.auto_submit(part1, part2)