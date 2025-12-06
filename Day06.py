from aocAuto import AOC_Auto

aoca = AOC_Auto(day=6, year=2025)

def parse(text):
    lines = text.split("\n")

    def remove_double_empty_spaces(line):
        while "  " in line:
            line = line.replace("  ", " ")
        return line

    numbers = [list(map(lambda x: int(x), remove_double_empty_spaces(line).strip().split(" "))) for line in lines[:-1]]
    operator_list = remove_double_empty_spaces(lines[-1]).strip().split(" ")
    return numbers, operator_list

def part1(input):
    numbers, operator_list = parse(input)
    math_result =[0 if operator == "+" else 1 for operator in operator_list]
    for ind, operator in enumerate(operator_list):
        if operator == "+":
            for number_list in numbers:
                math_result[ind] += number_list[ind]
        elif operator == "*":
            for number_list in numbers:
                math_result[ind] *= number_list[ind]
    return sum(math_result)
def part2(input):
    line_ended = True
    lines = input.split("\n")
    results = []
    for ind in range(len(lines[0])):
        if line_ended:
            numbers_col = []
        line_ended = True
        number = ""
        for line in lines:
            if not line[ind] in " +*":
                line_ended = False
                number += line[ind]
            if line[ind] in "*+":
                operator = line[ind]

        if not line_ended:
            numbers_col.append( int(number) )
        else:
            if operator == "*":
                result = 1
                for number in numbers_col:
                    result *= number
            elif operator == "+":
                result = 0
                for number in numbers_col:
                    result += number
            results.append(result)
    if not line_ended:
        if operator == "*":
            result = 1
            for number in numbers_col:
                result *= number
        elif operator == "+":
            result = 0
            for number in numbers_col:
                result += number
        results.append(result)
    return sum(results)

aoca.auto_submit(part1, part2)