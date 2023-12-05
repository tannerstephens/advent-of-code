from string import ascii_letters

from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    PRIORITIES = {c: i + 1 for i, c in enumerate(ascii_letters)}

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        return sum(self.PRIORITIES[(set(l[: len(l) // 2]) & set(l[len(l) // 2 :])).pop()] for l in p.lines())

    def part2(self, puzzle_input: str):
        p = Processing(puzzle_input)

        return sum(self.PRIORITIES[(s1 & s2 & s3).pop()] for s1, s2, s3 in p.grouped_lines(3, set))
