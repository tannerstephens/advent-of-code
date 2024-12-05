from collections import defaultdict
from re import compile

from garland import BaseSolution, PuzzleInput


def count(s: str):
    return s.count("XMAS") + s.count("SAMX")


class Solution(BaseSolution):
    PART2_DEPENDS_ON_PART1 = True

    def part1(self, puzzle_input: PuzzleInput):
        self.diagonal = defaultdict(str)
        self.diagonal2 = defaultdict(str)
        columns = defaultdict(str)

        grid = puzzle_input.splitlines()

        self.width = len(grid[0])
        self.height = len(grid)

        t = 0

        for y, row in enumerate(grid):
            t += count(row)
            for x, c in enumerate(row):
                columns[x] += c
                self.diagonal[x+y] += c
                self.diagonal2[y-x] += c

        for col in columns.values():
            t += count(col)

        for diag in self.diagonal.values():
            t += count(diag)

        for diag in self.diagonal2.values():
            t += count(diag)

        return t


    def part2(self, _: PuzzleInput):
        mas_regex = compile(r"(?=(MAS|SAM))")

        d1_mas_centers = set()

        for i, diag in enumerate(self.diagonal.values()):
            sx = min(self.width - 1, i)
            sy = max(0, i - self.width + 1)

            for match in mas_regex.finditer(diag):
                off = (match.start() + 1)
                d1_mas_centers.add((sx - off, sy + off))

        d2_mas_centers = set()

        diagonal2 = [d[1] for d in sorted(self.diagonal2.items(), key = lambda i: i[0])]

        for i, diag in enumerate(diagonal2):
            sx = max(0, self.width - 1 - i)
            sy = max(0, i - self.width + 1)

            for match in mas_regex.finditer(diag):
                off = (match.start() + 1)
                d2_mas_centers.add((sx + off, sy + off))

        return len(d1_mas_centers & d2_mas_centers)
