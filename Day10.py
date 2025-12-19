from aocAuto import AOC_Auto
import re  # regular expressions
import heapq

aoca = AOC_Auto(day=10, year=2025)


def parse(text):
    lines = text.split("\n")
    def get_machine(line):
        buttons = tuple(map(lambda s: tuple(map(int, s[1:-1].split(","))), re.findall(r'\([^)]*\)', line)))  # find ( ) and get any char in between that is not ). Zero or more times
        lights_on = tuple(map(lambda x: 1 if x == "#" else 0, re.findall(r'\[[^]]*\]', line)[0][1:-1]))  # lights are in [ ], and only once in the line
        joltage_req = tuple(map(int, re.findall(r'\{[^}]*\}', line)[0][1:-1].split(",")))  # joltage requirements are in { }, and only once in the line
        return (lights_on, buttons, joltage_req)

    return [get_machine(line) for line in lines]

def compute_neighbour_fun(buttons, num_joltages, validation_test = True):
    n = len(buttons)
    # compute all 2^n possible button combinations (to press each button at most once)
    # and filter, such that each state is only reached by the minimum amount of button presses
    all_btn_combs = {}
    for btn_comb in range(2 ** n):
        state = [0 for _ in range(num_joltages)]
        number_presses = 0
        for i, btn in enumerate(buttons):
            if btn_comb & (1 << i) != 0:  # if we press the i-th button
                number_presses += 1
                for ind in btn:
                    state[ind] += 1

        state = tuple(state)
        if state in all_btn_combs:
            all_btn_combs[state] = min(number_presses, all_btn_combs[state])
        else:
            all_btn_combs[state] = number_presses

    def get_all_normalization(joltage):
        neighbours = []
        for resulting_state, number_presses in all_btn_combs.items():
            new_joltage = [j - rs for j, rs in zip(joltage, resulting_state)]
            is_valid = True
            for ind, j in enumerate(new_joltage):
                if (validation_test and (j < 0)) or j % 2 != 0:  # if we do a validation test and its invalid (overshoot)or no normalization
                    is_valid = False
                    break
                new_joltage[ind] = j // 2
            if is_valid:
                neighbours.append((number_presses, tuple(new_joltage)))
        return neighbours

    return get_all_normalization



def part1(input):
    def get_fewest_presses(machine):
        lights_on, buttons, _ = machine
        get_all_normalization = compute_neighbour_fun(buttons, len(lights_on), False)
        return min(number_presses for number_presses, _ in get_all_normalization(lights_on))

    machines = parse(input)
    return sum(get_fewest_presses(machine) for machine in machines)


def get_minimum_presses(joltage_req, neighbour_fun):
    start_state = (0, 1, joltage_req)  # number_presses, factor, joltage
    heap = [start_state]
    seen = {}  # maps (factor, joltage) to min_costs

    while heap:
        number_presses, factor, joltage = heapq.heappop(heap)
        seen_state = (factor, joltage)

        if seen_state in seen and number_presses > seen[seen_state]:
            continue

        if sum(joltage) == 0:
            return number_presses

        for next_number_presses, new_joltage in neighbour_fun(joltage):
            new_number_presses = number_presses + next_number_presses * factor
            new_factor = 2 * factor
            new_seen_state = (new_factor, new_joltage)

            if new_seen_state in seen and new_number_presses >= seen[new_seen_state]:
                continue

            heapq.heappush(heap, (new_number_presses, new_factor, new_joltage))
            seen[new_seen_state] = new_number_presses
    return None


def part2(input):
    machines = parse(input)
    total_presses = 0
    for _, buttons, joltage_req in machines:
        get_all_normalization = compute_neighbour_fun(buttons, len(joltage_req))
        total_presses += get_minimum_presses(joltage_req, get_all_normalization)
    return total_presses

aoca.auto_submit(part1, part2)