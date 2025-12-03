from aocAuto import AOC_Auto

aoca = AOC_Auto(day=2, year=2025)

def parse(text):
    def str_tuple_to_int(line):
        values_str = line.split("-")
        return (int(values_str[0]), int(values_str[1]))
    ranges_str = text.split(",")
    ranges = [str_tuple_to_int(entry) for entry in ranges_str]
    return ranges

def check_range(id_start, id_end, valid_func):
    sum_invalid_ids = 0
    for id in range(id_start, id_end+1):
        if valid_func(id):
            sum_invalid_ids += id
    return sum_invalid_ids

def part1(input):
    ranges = parse(input)

    def valid_func(id):
        id_str = str(id)
        mid_ind = len(id_str) // 2
        return id_str[:mid_ind] == id_str[mid_ind:]

    sum_invalid_ids = 0
    for interval in ranges:
        sum_invalid_ids += check_range(*interval, valid_func)
    return sum_invalid_ids

def part2(input):
    ranges = parse(input)

    def valid_func(id):
        id_str = str(id)
        N = len(id_str)
        for times in range(2, N+1):
            if N % times != 0:
                continue
            part_len = N // times
            compare_base = id_str[:part_len]
            is_repeated = True
            for i in range(1,times):
                if not id_str[i*part_len:(i+1)*part_len] == compare_base:
                    is_repeated = False
                    break
            if not is_repeated:
                continue
            # otherwise its repreated {times} times.
            return True
        return False    # if every times it failed (its not repeated)

    sum_invalid_ids = 0
    for interval in ranges:
        sum_invalid_ids += check_range(*interval, valid_func)
    return sum_invalid_ids

aoca.auto_submit(part1, part2)