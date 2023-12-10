from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from .processing import Processing


class Grid:
    def __init__(self, puzzle_input: "Processing") -> None:
        self.grid = puzzle_input.lines(str)

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
