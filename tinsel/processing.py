import re
from typing import Callable, Generator


class Processing:
    def __init__(self, puzzle_input: str):
        self.puzzle_input = puzzle_input.strip()

    def integers(self) -> Generator[int, None, None]:
        for line in self.lines:
            try:
                yield int(line)
            except:
                yield None

    def count(self, s: str) -> int:
        return self.puzzle_input.count(s)

    def search[
        T
    ](self, regex: str, mapping: Callable[[str], T] | None = None, group=False) -> list[
        T
    ]:
        mapping = mapping or str

        compiled_regex = re.compile(regex)

        return [
            mapping(compiled_regex.search(line).group(group)) for line in self.lines
        ]

    def findall[
        T
    ](self, regex: str, mapping: Callable[[str], T] | None = None) -> list[list[T]]:
        mapping = mapping or str

        compiled_regex = re.compile(regex)

        return [
            [mapping(val) for val in match]
            for match in [compiled_regex.findall(line) for line in self.lines]
        ]

    def grouped_chars(self, n: int) -> list[tuple[str, ...]]:
        return zip(*[iter(self.puzzle_input)] * n)

    def to_map(self) -> list[list[str]]:
        m = []

        for line in self.puzzle_input:
            m.append(list(line))

        return m

    @property
    def lines(self):
        return self.puzzle_input.splitlines()

    def grouped_lines(self, n: int) -> list[tuple[str, ...]]:
        return zip(*[iter(self.lines)] * n)

    def __getitem__(self, key):
        return self.puzzle_input[key]

    def __iter__(self):
        return iter(self.puzzle_input)
