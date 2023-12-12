from collections import UserString
from functools import cached_property
from re import Match
from re import compile as re_compile
from typing import Callable, Generator, Iterator

from .grid import Grid


class Processing(UserString):
    def __init__(self, seq: object) -> None:
        if isinstance(seq, str):
            seq = seq.strip()

        super().__init__(seq)

        self._lines_cache = {}

    @cached_property
    def is_multiline(self):
        return "\n" in self.data

    def lines[T](self, mapping: Callable[[str], T] = str) -> list[T]:
        mapping = mapping or Processing

        key = str(type(mapping("")))

        if key not in self._lines_cache:
            self._lines_cache[key] = [mapping(line) for line in self.splitlines()]

        return self._lines_cache[key]

    def grouped_lines[T](self, n: int = 2, mapping: Callable[[str], T] = str) -> list[list[T]]:
        return zip(*[iter(self.lines(mapping=mapping))] * n)

    def re_findall[T](self, regex: str, mapping: Callable[[str], T] = str) -> list[list[T]] | list[T]:
        compiled_regex = re_compile(regex)

        if not self.is_multiline:
            return [mapping(match) for match in compiled_regex.findall(self.data)]

        return [[mapping(match) for match in compiled_regex.findall(line)] for line in self.lines(str)]

    def re_search[T](self, regex: str, group: int = 0, mapping: Callable[[str], T] = str) -> list[T] | T:
        compiled_regex = re_compile(regex)

        if not self.is_multiline:
            return mapping(compiled_regex.search(self.data).group(group))

        return [mapping(compiled_regex.search(line).group(group)) for line in self.lines(str)]

    def re_split[T](self, regex: str, mapping: Callable[[str], T] = str) -> list[list[T]] | list[T]:
        compiled_regex = re_compile(regex)

        if not self.is_multiline:
            return [mapping(elem) for elem in compiled_regex.split(self.data)]

        return [[mapping(elem) for elem in compiled_regex.split(line)] for line in self.lines(str)]

    def re_finditer(self, regex: str) -> list[Iterator[Match[str]]] | Iterator[Match[str]]:
        compiled_regex = re_compile(regex)

        if not self.is_multiline:
            return compiled_regex.finditer(self.data)

        return [compiled_regex.finditer(line) for line in self.lines(str)]

    def to_grid(self):
        return Grid(self)

    def integers(self) -> Generator[int, None, None]:
        for line in self.lines(str):
            yield (int(line))

    def split_each_line[
        T
    ](self, sep: str | None = None, mapping: Callable[[str], T] = str) -> Generator[
        Generator[T, None, None], None, None
    ]:
        for line in self.lines():
            yield map(mapping, line.split(sep))

    def counts(self):
        counts = {}

        for c in set(self.data):
            counts[c] = self.count(c)

        return counts

    def split[
        T
    ](
        self,
        sep: str | None = None,
        maxsplit: int = -1,
        mapping: Callable[[str], T] = str,
    ) -> Generator[
        T, None, None
    ]:
        for seg in super().split(sep, maxsplit):
            yield mapping(seg)
