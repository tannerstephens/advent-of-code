from itertools import combinations

from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        grid = p.to_grid()

        no_gal_rows = set(y for y in range(len(grid.grid)))
        no_gal_cols = set(x for x in range(len(grid.grid[0])))

        galaxies = []

        for y, row in enumerate(grid.rows()):
            for x, c in enumerate(row):
                if c == "#":
                    galaxies.append((x, y))
                    no_gal_rows.discard(y)
                    no_gal_cols.discard(x)

        self.total_distance = 0
        self.extra_distance = 0

        for i, (gx1, gy1) in enumerate(galaxies):
            for gx2, gy2 in galaxies[i + 1 :]:
                wgx1 = gx1
                if gx2 < wgx1:
                    wgx1, gx2 = gx2, wgx1

                dup_rows = len([y for y in no_gal_rows if gy1 < y < gy2])
                dup_cols = len([x for x in no_gal_cols if wgx1 < x < gx2])

                self.extra_distance += dup_rows + dup_cols
                self.total_distance += (gx2 - wgx1) + (gy2 - gy1)

        return self.total_distance + self.extra_distance

    def part2(self, puzzle_input: str):
        return self.total_distance + self.extra_distance * 999999
