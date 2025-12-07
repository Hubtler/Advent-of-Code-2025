from aocAuto import AOC_Auto

aoca = AOC_Auto(day=6, year=2025)

def parse(text):
    lines = text.split("\n")
    blocks = [list(map(lambda x: int(x), line.split())) for line in lines[:-1]]
    operator_list = lines[-1].split()
    return blocks, operator_list

def transpose(lines):
    return "\n".join(["".join([line[ind] for line in lines]).strip() for ind in range(len(lines[0]))])

def parse_colwise(text):
    lines = text.split("\n")
    operators = [c for c in lines[-1] if c != " "]
    cols = transpose(lines[:-1])
    blocks_str = cols.split("\n\n")
    blocks = [[int(c) for c in block.split("\n")] for block in blocks_str]
    return blocks, operators


def part1(input):
    blocks, operator_list = parse(input)
    total = 0
    for ind, operator in enumerate(operator_list):
        result = 0
        if operator == "+":
            for block in blocks:
                result += block[ind]
        elif operator == "*":
            result = 1
            for block in blocks:
                result *= block[ind]
        total += result
    return total

def part2(input):
    blocks, operators = parse_colwise(input)
    total = 0
    for block, operator in zip(blocks, operators):
        result = 0
        if operator == "+":
            for number in block:
                result += number
        elif operator == "*":
            result = 1
            for number in block:
                result *= number
        total += result
    return total


aoca.auto_submit(part1, part2)