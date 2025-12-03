from aocAuto import AOC_Auto
import numpy as np

aoca = AOC_Auto(day = 3, year = 2025)

def parse(text):
    lines = text.split("\n")
    return [[int(c) for c in line] for line in lines]

def get_joltage( bank, N_turn_on ):
    if N_turn_on == 1:
        return max(bank)
    biggest_ind = np.argmax(bank[:-(N_turn_on-1)])
    return bank[biggest_ind] * 10**(N_turn_on-1) + get_joltage(bank[ biggest_ind + 1: ], N_turn_on-1)

def part1(input):
    battery_banks = parse(input)
    return sum( map( lambda bank: get_joltage(bank, 2), battery_banks ) )

def part2(input):
    battery_banks = parse(input)
    return sum(map(lambda bank: get_joltage(bank, 12), battery_banks))

aoca.auto_submit(part1, part2)