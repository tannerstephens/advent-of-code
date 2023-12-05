from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.digits = p.re_findall(f"\d+", int)

        return sum((e1l <= e2l and e1r >= e2r) or (e2l <= e1l and e2r >= e1r) for e1l, e1r, e2l, e2r in self.digits)

    def part2(self, puzzle_input: str):
        return sum((e1l <= e2r) and (e2l <= e1r) for e1l, e1r, e2l, e2r in self.digits)
