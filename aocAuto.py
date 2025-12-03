from aocd import submit, get_day_and_year
from aocd.models import Puzzle

class AOC_Auto:
    def __init__(self, day = None, year = None, skip_example_part_a = False, skip_example_part_b = False):
        if day is None or year is None:
            detected_day, detected_year = get_day_and_year()
            day = detected_day if day is None else day
            year = detected_year if year is None else year
        self.day = day
        self.year = year
        self.skip_example_part_a = skip_example_part_a
        self.skip_example_part_b = skip_example_part_b

        self.puzzle = Puzzle(day = self.day, year = self.year)

    def test_part_a(self, part1, console_output = False):
        # part1(input_string) -> output_value
        passed_all_tests = True
        for example in self.puzzle.examples:
            if example.answer_a is None:
                continue
            own_output = str(part1(example.input_data))
            if own_output is None:
                if console_output:
                    print("Part 1 returns", own_output)
                return False
            if not own_output == example.answer_a:
                passed_all_tests = False
                if console_output:
                    print("Got an example for part 1 wrong. Auto-submit off, example output: ", example.answer_a, "my output:", own_output)
            elif console_output:
                    print("Example for part 1 correct, result: ", own_output)
        return passed_all_tests

    def test_part_b(self, part2, console_output = False):
        # part2(input_string) -> output_value
        passed_all_tests = True
        for example in self.puzzle.examples:
            if example.answer_b is None:
                continue
            own_output = str(part2(example.input_data))
            if own_output is None:
                if console_output:
                    print("Part 2 returns", own_output)
                return False
            if not own_output == example.answer_b:
                passed_all_tests = False
                if console_output:
                    print("Got an example for part 2 wrong. Auto-submit off, example output: ", example.answer_b, "my output:", own_output)
            elif console_output:
                print("Example for part 2 correct, result: ", own_output)
        return passed_all_tests

    def auto_submit_a(self, part1, console_output = False):
        if self.skip_example_part_a or self.test_part_a(part1, console_output):
            own_solution = part1(self.puzzle.input_data)
            submit(own_solution, part="a", day=self.day, year=self.year)

    def auto_submit_b(self, part2, console_output = False):
        if self.skip_example_part_b or self.test_part_b(part2, console_output):
            own_solution = part2(self.puzzle.input_data)
            submit(own_solution, part="b", day=self.day, year=self.year)

    def auto_submit(self, part1, part2, console_output = False):
        self.auto_submit_a(part1, console_output)
        self.auto_submit_b(part2, console_output)

