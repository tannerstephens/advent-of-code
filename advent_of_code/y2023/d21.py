from tinsel import BFS, BaseSolution, Grid, InfiniteGrid
from tinsel.grid import Grid
from tinsel.processing import Processing


class GardenWalk(BFS):
    def __init__(self, grid_map: str | Processing | Grid, stop=None) -> None:
        super().__init__(grid_map)
        self.stop = stop

    def valid_pos(self, cx: int, cy: int, nx: int, ny: int, distances: dict[tuple[int, int], int]) -> int:
        if self.stop is not None and distances[cx, cy] >= self.stop:
            return False

        return self.grid_map.get(nx, ny) != "#"


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        g = Grid(puzzle_input)

        self.sx = self.sy = None

        for y, row in enumerate(g.rows()):
            for x, c in enumerate(row):
                if c == "S":
                    self.sx, self.sy = x, y
                    break

            if self.sx:
                break

        return sum(1 for v in GardenWalk(g, 64).calculate(self.sx, self.sy).values() if ((v % 2 == 0)))

    def part2(self, puzzle_input: str):
        g = Grid(puzzle_input)

        distances = GardenWalk(g).calculate(self.sx, self.sy).values()

        distance_from_center = (g.width - 1) // 2

        even_count = 0
        odd_count = 0
        even_corner_count = 0
        odd_corner_count = 0

        for v in distances:
            if parity := v % 2:
                odd_count += 1
            else:
                even_count += 1

            if v > distance_from_center:
                if parity:
                    odd_corner_count += 1
                else:
                    even_corner_count += 1

        num_squares_in_line = (26501365 - distance_from_center) // (g.width)

        return (
            pow(num_squares_in_line + 1, 2) * odd_count
            + pow(num_squares_in_line, 2) * even_count
            - (num_squares_in_line + 1) * odd_corner_count
            + num_squares_in_line * even_corner_count
        )
