from collections import deque

from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def diff(self, values: list[int]) -> list[int]:
        return [values[i + 1] - values[i] for i in range(0, len(values) - 1)]

    def multi_diff(self, values: list[int]) -> list[list[int]]:
        diffs = [values]

        while not all(d == diffs[-1][0] for d in diffs[-1]):
            diffs.append(self.diff(diffs[-1]))

        return diffs

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.processed_values = p.re_findall(r"-?\d+", mapping=int)

        s = 0

        self.diffs = []

        for line in self.processed_values:
            diffs = self.multi_diff(line)[::-1]
            self.diffs.append(diffs)

            d = 0

            for diff in diffs:
                d = diff[-1] + d

            s += d

        return s

    def part2(self, puzzle_input: str):
        s = 0

        for diffs in self.diffs:
            d = 0

            for diff in diffs:
                d = diff[0] - d

            s += d

        return s
