import heapq
from typing import Callable

from tinsel.grid import Grid
from tinsel.processing import Processing


class PriorityQueue[T]:
    def __init__(self):
        self.elements: list[tuple[float, T]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]


class BFS[T]:
    DEFAULT_MAPPING: Callable[[str], T] = str

    def __init__(self, grid_map: str | Processing | Grid[T]) -> None:
        if type(grid_map) is Processing:
            grid_map = grid_map.to_grid(mapping=self.DEFAULT_MAPPING)
        elif type(grid_map) is str:
            grid_map = Grid(grid_map, mapping=self.DEFAULT_MAPPING)

        self.grid_map: Grid[T] = grid_map

    def new_distance(self, cx: int, cy: int, nx: int, ny: int, distances: dict[tuple[int, int], int]) -> int:
        return distances[cx, cy] + 1

    def valid_pos(self, cx: int, cy: int, nx: int, ny: int, distances: dict[tuple[int, int], int]) -> int:
        return True

    def calculate(self, x0: int, y0: int):
        frontier: PriorityQueue[tuple[int, int]] = PriorityQueue()
        frontier.put((x0, y0), 0)

        distances = {(x0, y0): 0}

        while not frontier.empty():
            cx, cy = frontier.get()

            for nx, ny in self.grid_map.neighbor_coords(cx, cy, corners=False):
                if self.valid_pos(cx, cy, nx, ny, distances):
                    new_distance = self.new_distance(cx, cy, nx, ny, distances)
                    if (nx, ny) not in distances or new_distance < distances[nx, ny]:
                        distances[nx, ny] = new_distance
                        frontier.put((nx, ny), new_distance)

        return distances
