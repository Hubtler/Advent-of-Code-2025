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
    biggest_val = bank[biggest_ind]
    return biggest_val * 10**(N_turn_on-1) + get_joltage(bank[ biggest_ind + 1: ], N_turn_on-1)


def part1(input):
    battery_banks = parse(input)
    total_joltage = 0
    for bank in battery_banks:
        joltage = get_joltage(bank, 2)
        total_joltage += joltage
    return total_joltage


def part2(input):
    battery_banks = parse(input)
    total_joltage = 0
    for bank in battery_banks:
        joltage = get_joltage(bank, 12)
        total_joltage += joltage
    return total_joltage

aoca.auto_submit(part1, part2)
