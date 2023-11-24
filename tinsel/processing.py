import re
from typing import Any, Callable


class Processing:
    def __init__(self, puzzle_input: str):
        self.puzzle_input = puzzle_input

    def integers(self) -> list[int]:
        return [int(line) for line in self.puzzle_input.splitlines()]

    def count(self, s: str) -> int:
        return self.puzzle_input.count(s)

    def regex[
        T
    ](self, regex: str, mapping: Callable[[str], T] | None = None) -> list[list[T]]:
        mapping = mapping or str

        return [
            [mapping(val) for val in match]
            for match in [
                re.findall(regex, line) for line in self.puzzle_input.splitlines()
            ]
        ]

    def __getitem__(self, key):
        return self.puzzle_input[key]

    def __iter__(self):
        return iter(self.puzzle_input)
