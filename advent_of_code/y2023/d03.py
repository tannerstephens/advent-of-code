from collections import defaultdict

from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    SYMBOLS = set("!@#$%^&*()_+-=/")

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        grid = p.to_grid()

        s = 0

        self.state.gears = defaultdict(list)

        for y, line in enumerate(p.re_finditer(r"\d+")):
            for match in line:
                x = match.start()

                for c, cx, cy in grid.indexed_neighbors(x, y, bw=(match.end() - x)):
                    if c in self.SYMBOLS:
                        s += (val := int(match.group(0)))
                        if c == "*":
                            self.state.gears[(cx, cy)].append(val)

                        break

        return s

    def part2(self, puzzle_input: str):
        return sum(parts[0] * parts[1] for parts in self.state.gears.values() if len(parts) == 2)
