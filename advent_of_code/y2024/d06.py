from garland import BaseSolution, Maze, PuzzleInput
from garland.maze import MazeType
from garland.utils import *


class MapStatus(Enum):
    COMPLETED = "completed"
    LOOPED = "looped"
    WALL = "wall"



class Map(Maze):
    def __init__(self, puzzle_input: PuzzleInput, type_mapping: dict[str, MazeType] | None = None) -> None:
        self.direction = Direction.NORTH

        self.visited = set()
        self.visited_dir: set[tuple[int, int, Direction]] = set()

        super().__init__(puzzle_input, type_mapping)

        self.visited.add(self.position)
        self.visited_dir.add((*self.position, self.direction))

    def run_to_edge(self):
        while (status := self.forward()) is MapStatus.WALL:
            pass

        return status

    def forward(self):
        dx, dy = self.direction.delta

        while (n := self.grid[self.py + dy][self.px + dx]) is MazeType.EMPTY:
            self.px += dx
            self.py += dy

            self.visited.add(self.position)

            if (*self.position, self.direction) in self.visited_dir:
                return MapStatus.LOOPED

            self.visited_dir.add((*self.position, self.direction))

        if n is MazeType.EDGE:
            return MapStatus.COMPLETED

        self.direction = self.direction.right

        if (*self.position, self.direction) in self.visited_dir:
            return MapStatus.LOOPED

        self.visited_dir.add((*self.position, self.direction))

        return MapStatus.WALL

    def check_for_loop(self, ox: int, oy: int):
        self.visited_dir = set()

        self.grid[oy][ox] = MazeType.WALL

        status = self.run_to_edge()

        self.grid[oy][ox] = MazeType.EMPTY

        return status is MapStatus.LOOPED

    def find_loops(self):
        self.direction = Direction.NORTH

        old_vd = self.visited_dir

        loops = set()

        for (x, y, d) in old_vd:
            dx, dy = d.delta

            ox = x + dx
            oy = y + dy

            if ox == self.sx and oy == self.sy:
                continue

            if self.grid[oy][ox] is not MazeType.EMPTY:
                continue

            self.px = self.sx
            self.py = self.sy

            self.direction = Direction.NORTH

            if self.check_for_loop(ox, oy):
                loops.add((ox, oy))

        return len(loops)

class Solution(BaseSolution):
    PART2_DEPENDS_ON_PART1 = True

    def part1(self, puzzle_input: PuzzleInput):
        self.map = puzzle_input.as_maze(maze_class=Map)

        self.map.run_to_edge()

        return len(self.map.visited)

    def part2(self, puzzle_input: PuzzleInput):
        return self.map.find_loops()
