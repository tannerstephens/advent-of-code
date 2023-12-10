from tinsel import BaseSolution, Grid, Processing


class PipeGrid(Grid):
    PATHING = {
        "|": ((0, 1, 0, -1)),
        "-": ((1, 0, -1, 0)),
        "L": ((0, -1, 1, 0)),
        "J": ((0, -1, -1, 0)),
        "7": ((-1, 0, 0, 1)),
        "F": ((1, 0, 0, 1)),
    }

    def __init__(self, puzzle_input: str) -> None:
        p = Processing(puzzle_input)

        self.grid = {}
        self.start = None
        self.groud = set()

        for y, line in enumerate(p.lines()):
            for x, c in enumerate(line):
                if c in self.PATHING:
                    dx1, dy1, dx2, dy2 = self.PATHING[c]

                    one = (x + dx1, y + dy1)
                    two = (x + dx2, y + dy2)

                    self.grid[(x, y)] = {one: two, two: one}
                elif c == "S":
                    self.start = (x, y)
                else:
                    self.groud.add((x, y))

    def get(self, x: int, y: int):
        return self.grid[(x, y)]

    def coord_in_grid(self, x: int, y: int) -> bool:
        return (x, y) in self.grid

    def __contains__(self, elem):
        return elem in self.grid


class Solution(BaseSolution):
    def loop_length(self, pipe_grid: PipeGrid, x: int, y: int) -> tuple[int, list[tuple[int, int]]] | None:
        last_x, last_y = pipe_grid.start

        length = 1
        points = [(x, y)]

        while (x, y) != pipe_grid.start:
            if (x, y) not in pipe_grid:
                return None

            length += 1
            tx, ty = x, y
            x, y = pipe_grid.get(x, y)[(last_x, last_y)]
            points.append((x, y))
            last_x, last_y = tx, ty

        return length, points

    def part1(self, puzzle_input: str):
        self.pipe_grid = PipeGrid(puzzle_input)

        for x, y in self.pipe_grid.neighbor_coords(*self.pipe_grid.start):
            if l := self.loop_length(self.pipe_grid, x, y):
                self.loop_points = l[1]
                return l[0] // 2

    def part2(self, puzzle_input: str):
        top = 0

        self.loop_points.append(self.loop_points[0])

        for i, (x1, y1) in enumerate(self.loop_points[:-1]):
            x2, y2 = self.loop_points[i + 1]

            top += x1 * y2 - y1 * x2

        area = abs(top // 2)

        return area + 1 - (len(self.loop_points) // 2)
