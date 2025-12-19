from aocAuto import AOC_Auto

aoca = AOC_Auto(day=12, year=2025, skip_example_part_a=True)

def parse(text):
    text_parts = text.split("\n\n")

    def parse_shape(text_block):
        lines = text_block.split("\n")
        blocked_coordinates = []
        for i, line in enumerate(lines[1:]): # in zeros line is only id
            for j, c in enumerate(line):
                if c == "#":
                    blocked_coordinates.append((i,j))
        return blocked_coordinates
    shapes = [parse_shape(text_part) for text_part in text_parts[:-1]]

    def parse_region(line):
        parts = line.split(": ")
        amounts = list( map(int, parts[1].split(" ")) )
        height, width,  = map(int, parts[0].split("x"))
        return (height, width, amounts)
    regions = [parse_region(line) for line in text_parts[-1].split("\n")]

    return shapes, regions


def part1(input):
    shapes, regions = parse(input)
    number_fit = 0
    for height, width, amounts in regions:
        lower_bound = (height // 3) * (width // 3) # so many packets can be placed inside for sure
        if lower_bound >= sum(amounts):
            number_fit += 1
            continue
        total_space = height*width
        space_needed = sum( [amount*len(shape) for amount, shape in zip(amounts, shapes)] ) # total number of blocked spaces
        if space_needed > total_space:
            continue
        # otherwise we need to fit it
        print(f"Does it fit? {amounts} in {height}x{width}?")
    return number_fit

aoca.auto_submit_a(part1, console_output=True)