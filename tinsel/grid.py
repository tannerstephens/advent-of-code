import math
from typing import TYPE_CHECKING, Callable, Generator, Union

if TYPE_CHECKING:
    from .processing import Processing


class Grid[T]:
    def __init__(
        self, puzzle_input: Union["Processing", str, list[list[T]]], mapping: Callable[[str], T] = str
    ) -> None:
        if type(puzzle_input) is list:
            self.grid = puzzle_input
        else:
            self.grid: list[list[T]] = [[mapping(c) for c in line] for line in puzzle_input.splitlines()]

    def get_candidates(self, corners: bool, bw: int, bh: int) -> Generator[tuple[int, int], None, None]:
        for dx in range(bw):
            yield (dx, -1)
            yield (dx, bh)

        for dy in range(bh):
            yield (-1, dy)
            yield (bw, dy)

        if corners:
            yield (-1, -1)
            yield (-1, bh)
            yield (bw, -1)
            yield (bw, bh)

    def coord_in_grid(self, x: int, y: int) -> bool:
        return 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid)

    def neighbor_coords(
        self, x: int, y: int, corners=True, bw: int = 1, bh: int = 1
    ) -> Generator[tuple[int, int], None, None]:
        for dx, dy in self.get_candidates(corners, bw, bh):
            tx = x + dx
            ty = y + dy

            if self.coord_in_grid(tx, ty):
                yield (tx, ty)

    def indexed_neighbors(
        self, x: int, y: int, corners=True, bw: int = 1, bh: int = 1
    ) -> Generator[tuple[str, int, int], None, None]:
        for tx, ty in self.neighbor_coords(x, y, corners, bw, bh):
            yield self.get(tx, ty), tx, ty

    def neighbors(self, x: int, y: int, corners=True, bw: int = 1, bh: int = 1) -> Generator[str, None, None]:
        for tx, ty in self.neighbor_coords(x, y, corners, bw, bh):
            yield self.get(tx, ty)

    @property
    def width(self):
        return len(self.grid[0])

    @property
    def height(self):
        return len(self.grid)

    def get(self, x: int, y: int):
        return self.grid[y][x]

    def rows(self):
        return iter(self.grid)

    def columns(self):
        for x in range(len(self.grid[0])):
            yield [line[x] for line in self.grid]

    def horizontal_split(self, row: int) -> tuple["Grid", "Grid"]:
        return Grid(self.grid[:row]), Grid(self.grid[row:])

    def __getitem__(self, elem):
        return self.grid[elem]

    def __repr__(self):
        return "\n".join("".join(str(c) for c in line) for line in self.grid)

    def copy(self):
        return Grid(repr(self))

    def __len__(self):
        return len(self.grid)
