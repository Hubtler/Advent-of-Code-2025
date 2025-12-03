from aocd import get_data, submit

auto_submit_1 = True
auto_submit_2 = True
day = 1
text = get_data(day=day, year=2025)
# parsing
def get_value(rotation):
    direction = rotation[0]
    distance = int(rotation[1:])
    if direction == "L":
        return -distance
    return distance

circle_len = 100
dial_pos = 50
lines = text.split("\n")
moves = [get_value(line) for line in lines]

sum_zero_pointings = 0
sum_zero_pointings_inbetween = 0
for move in moves:
    old_dial_pos = dial_pos
    dial_pos += move
    mul = dial_pos // circle_len
    if old_dial_pos == 0 and mul < 0:
        mul += 1
    sum_zero_pointings_inbetween += abs(mul)
    if dial_pos == 0:   # if we are at zero at the end, add +1
        sum_zero_pointings_inbetween += 1
    if dial_pos < 0 and dial_pos % circle_len == 0: # if we are at -100, -200 or something like that, mul counts one less than expected (from 85 to -400 are over 0,-100,-200,-300,-400 so 5 times. but mul == 4)
        sum_zero_pointings_inbetween += 1
    dial_pos %= circle_len
    if dial_pos == 0:
        sum_zero_pointings += 1

part1 = sum_zero_pointings
if auto_submit_1:
    submit(part1, part="a", day=day, year=2025)
else:
    print(f"Part 1: {part1}")

part2 = sum_zero_pointings_inbetween
if auto_submit_2:
    submit(part2, part="b", day=day, year=2025)
else:
    print(f"Part 2: {part2}")
