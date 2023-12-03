from collections import UserString
from functools import cached_property
from re import compile as re_compile
from typing import Callable


class Processing(UserString):
    def __init__(self, seq: object) -> None:
        if isinstance(seq, str):
            seq = seq.strip()

        super().__init__(seq)

        self._lines_cache = {}

    @cached_property
    def is_multiline(self):
        return "\n" in self.data

    def lines[T](self, mapping: Callable[[str], T] | None = None) -> list[T]:
        mapping = mapping or Processing

        key = str(type(mapping("")))

        if key not in self._lines_cache:
            self._lines_cache[key] = [mapping(line) for line in self.splitlines()]

        return self._lines_cache[key]

    def re_findall[
        T
    ](self, regex: str, mapping: Callable[[str], T] | None = None) -> (
        list[list[T]] | list[T]
    ):
        compiled_regex = re_compile(regex)

        mapping = mapping or str

        if not self.is_multiline:
            return [mapping(match) for match in compiled_regex.findall(self.data)]

        return [
            [mapping(match) for match in compiled_regex.findall(line)]
            for line in self.lines(str)
        ]

    def re_search[
        T
    ](self, regex: str, group: int = 0, mapping: Callable[[str], T] | None = None) -> (
        list[T] | T
    ):
        compiled_regex = re_compile(regex)

        mapping = mapping or str

        if not self.is_multiline:
            return mapping(compiled_regex.search(self.data).group(group))

        return [
            mapping(compiled_regex.search(line).group(group))
            for line in self.lines(str)
        ]
