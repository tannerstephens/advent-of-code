from enum import Enum
from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .puzzle_input import PuzzleInput


class MazeType(Enum):
    EMPTY = "empty"
    WALL = "wall"
    EDGE = "edge"

    def __str__(self):
        match self:
            case MazeType.EMPTY:
                return " "
            case MazeType.WALL:
                return "#"
            case MazeType.EDGE:
                return "%"




DEFAULT_TYPE_MAPPING = {
    ".": MazeType.EMPTY,
    '#': MazeType.WALL,
}


class Maze:
    def __init__(self, puzzle_input: "PuzzleInput", type_mapping: dict[str, MazeType] | None = None, starting_character: str = "^") -> None:
        type_mapping = type_mapping or DEFAULT_TYPE_MAPPING

        self.px: int = None
        self.py: int = None

        self.sx: int = None
        self.sy: int = None

        lines = puzzle_input.splitlines()

        self.grid: list[list[MazeType]] = [[MazeType.EDGE] * (len(lines[0]) + 2)]



        for y, row in enumerate(lines):
            self.grid.append([MazeType.EDGE])

            for x, c in enumerate(row):
                if c == starting_character:
                    self.sx = self.px = x + 1
                    self.sy = self.py = y + 1

                    self.grid[-1].append(MazeType.EMPTY)
                else:
                    self.grid[-1].append(type_mapping[c])

            self.grid[-1].append(MazeType.EDGE)

        self.grid.append([MazeType.EDGE] * (len(lines[0]) + 2))

    @property
    def position(self):
        return self.px, self.py

    @cached_property
    def max_x(self):
        return len()

    def __repr__(self):
        out = ""

        for row in self.grid:
            for c in row:
                out += str(c)

            out += "\n"

        return out
