from itertools import accumulate, cycle

from garland import BaseSolution, PuzzleInput


class Solution(BaseSolution):
    def part1(self, puzzle_input: PuzzleInput):
        return sum(puzzle_input.integers())


    def part2(self, puzzle_input: PuzzleInput):
        seen = {0}

        for f in accumulate(cycle(puzzle_input.integers())):
            if f in seen:
                return f

            seen.add(f)
