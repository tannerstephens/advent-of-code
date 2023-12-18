import sys

from tinsel import BaseSolution, Grid, Processing
from tinsel.consts import DIRS

sys.setrecursionlimit(10000)


class Solution(BaseSolution):
    NEW_DIRS = {
        0: {"\\": [3], "/": [1], "-": [1, 3]},
        1: {"\\": [2], "/": [0], "|": [0, 2]},
        2: {"\\": [1], "/": [3], "-": [1, 3]},
        3: {"\\": [0], "/": [2], "|": [0, 2]},
    }

    def beam(self, maze: Grid, x: int = -1, y: int = 0, d: int = 1, seen: set = None, dir_seen: set = None):
        if seen is None:
            seen = set()

        if dir_seen is None:
            dir_seen = set()

        dx, dy = DIRS[d]
        nx, ny = x + dx, y + dy

        if (nx, ny, d) in dir_seen:
            return 0

        if not maze.coord_in_grid(nx, ny):
            return 0

        dir_seen.add((nx, ny, d))
        seen.add((nx, ny))

        if (c := maze.get(nx, ny)) in self.NEW_DIRS[d]:
            for nd in self.NEW_DIRS[d][c]:
                self.beam(maze, nx, ny, nd, seen, dir_seen)
        else:
            self.beam(maze, nx, ny, d, seen, dir_seen)

        return len(seen)

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.maze = p.to_grid()

        return self.beam(self.maze)

    def part2(self, puzzle_input: str):
        mx = 0

        for y, d in ((-1, 2), (len(self.maze), 0)):
            for x in range(len(self.maze[0])):
                mx = max(mx, self.beam(self.maze, x, y, d))

        for x, d in ((-1, 1), (len(self.maze[0]), 3)):
            for y in range(len(self.maze)):
                mx = max(mx, self.beam(self.maze, x, y, d))

        return mx
