from math import ceil, floor, prod
from typing import cast

from tinsel import BaseSolution, Processing, Range


class Solution(BaseSolution):
    def get_win_range(self, length: int, record: int):
        rhs = pow((length * length) - (4 * record) - 4, 0.5)

        return Range(ceil(((length - rhs) / 2)), end=floor(((length + rhs) / 2)))

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.lengths, self.records = cast(list[list[str]], p.re_findall(r"\d+"))

        return prod(self.get_win_range(int(l), int(r)).length for l, r in zip(self.lengths, self.records))

    def part2(self, puzzle_input: str):
        length = int("".join(self.lengths))
        record = int("".join(self.records))

        return self.get_win_range(length, record).length
