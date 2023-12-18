import heapq
from functools import lru_cache

from tinsel import BaseSolution, Grid
from tinsel.consts import DIRS


class PriorityQueue[T]:
    def __init__(self):
        self.elements: list[tuple[float, T]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]


class Pathfinder:
    def __init__(self, g: Grid[int]) -> None:
        self.grid = g

    @lru_cache
    def new_ds(self, d: int | None, cdl: int, min_straight: int):
        if d is None:
            return [(0, 1), (1, 1), (2, 1), (3, 1)]
        elif cdl < min_straight:
            return [(d, cdl + 1)]
        else:
            return [((d - 1) % 4, 1), ((d + 1) % 4, 1), (d, cdl + 1)]

    def distance(self, x0: int, y0: int, x1: int, y1: int, max_straight=3, min_straight=0) -> int:
        frontier: PriorityQueue[tuple[int, int, int, int]] = PriorityQueue()
        frontier.put((x0, y0, None, None), 0)

        came_from = {}
        cost_so_far = {}

        came_from[x0, y0, None, None] = None
        cost_so_far[x0, y0, None, None] = 0

        sols = []

        while not frontier.empty():
            cx, cy, cd, cdl = frontier.get()

            if cx == x1 and cy == y1:
                sols.append(cost_so_far[cx, cy, cd, cdl])

            for nd, ndl in self.new_ds(cd, cdl, min_straight):
                if ndl > max_straight:
                    continue

                dx, dy = DIRS[nd]
                nx, ny = cx + dx, cy + dy

                if self.grid.coord_in_grid(nx, ny):
                    new_cost = cost_so_far[cx, cy, cd, cdl] + self.grid.get(nx, ny)
                    if ((nx, ny, nd, ndl) not in cost_so_far) or (new_cost < cost_so_far[nx, ny, nd, ndl]):
                        cost_so_far[nx, ny, nd, ndl] = new_cost
                        frontier.put((nx, ny, nd, ndl), new_cost)
                        came_from[nx, ny, nd, ndl] = (cx, cy)

        return min(sols)


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        g = Grid(puzzle_input, int)
        path_finder = Pathfinder(g)
        return path_finder.distance(0, 0, g.width - 1, g.height - 1)

    def part2(self, puzzle_input: str):
        g = Grid(puzzle_input, int)
        path_finder = Pathfinder(g)
        return path_finder.distance(0, 0, g.width - 1, g.height - 1, min_straight=4, max_straight=10)
