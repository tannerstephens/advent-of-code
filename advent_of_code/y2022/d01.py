from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.state.calories = sorted(sum(cal_group.integers()) for cal_group in p.split("\n\n", mapping=Processing))

        return self.state.calories[-1]

    def part2(self, puzzle_input: str):
        return sum(self.state.calories[-3:])
