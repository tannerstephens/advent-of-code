from tinsel import BaseSolution, Grid, Processing


class PipeGrid(Grid):
    PATHING: dict[str, tuple[int, int, int, int]] = {
        "|": (0, 1, 0, -1),
        "-": (1, 0, -1, 0),
        "L": (0, -1, 1, 0),
        "J": (0, -1, -1, 0),
        "7": (-1, 0, 0, 1),
        "F": (1, 0, 0, 1),
    }

    def __init__(self, puzzle_input: str) -> None:
        p = Processing(puzzle_input)

        self.grid = {}
        self.start = None

        for y, line in enumerate(p.lines()):
            for x, c in enumerate(line):
                if path := self.PATHING.get(c):
                    one = (x + path[0], y + path[1])
                    two = (x + path[2], y + path[3])

                    self.grid[(x, y)] = {one: two, two: one}
                elif c == "S":
                    self.start = (x, y)

    def get(self, x: int, y: int):
        return self.grid[(x, y)]

    def coord_in_grid(self, x: int, y: int) -> bool:
        return (x, y) in self.grid


class Solution(BaseSolution):
    def loop_length(self, pipe_grid: PipeGrid, x: int, y: int) -> list[tuple[int, int]] | None:
        last_x, last_y = pipe_grid.start

        points = [(x, y)]

        while (x, y) != pipe_grid.start:
            if not pipe_grid.coord_in_grid(x, y):
                return None

            (x, y), last_x, last_y = pipe_grid.get(x, y)[(last_x, last_y)], x, y

            points.append((x, y))

        return points

    def part1(self, puzzle_input: str):
        self.pipe_grid = PipeGrid(puzzle_input)

        for x, y in self.pipe_grid.neighbor_coords(*self.pipe_grid.start):
            if l := self.loop_length(self.pipe_grid, x, y):
                self.loop_points = l
                return len(l) // 2

    def part2(self, puzzle_input: str):
        # Pick's Formula
        top = 0

        num_points = len(self.loop_points)

        self.loop_points.append(self.loop_points[0])

        for i, (x1, y1) in enumerate(self.loop_points[:-1]):
            x2, y2 = self.loop_points[i + 1]

            top += x1 * y2 - y1 * x2

        return (top - num_points) // 2 + 1
