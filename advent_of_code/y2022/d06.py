from re import search

from tinsel import BaseSolution


class Solution(BaseSolution):
    def build_regex(self, n: int):
        regex = r"(.)"
        negating = r"\1"

        for i in range(1, n):
            regex += f"((?!{negating}).)"
            negating += f"|\\{i+1}"

        return regex

    def part1(self, puzzle_input: str):
        return search(self.build_regex(4), puzzle_input).end()

    def part2(self, puzzle_input: str):
        return search(self.build_regex(14), puzzle_input).end()
