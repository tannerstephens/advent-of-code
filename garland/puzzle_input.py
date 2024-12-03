from collections import UserString
from itertools import batched
from pathlib import Path
from re import compile
from typing import Generator

from garland.input_fetcher import InputFetcher

INTEGER_REGEX = compile(r"-?\d+")

class PuzzleInput(UserString):
    def __init__(self, data):
        if isinstance(data, str):
            data = data.strip()

        super().__init__(data)

    @classmethod
    def from_day(cls, year: int, day: int, cache_location: Path | None = None):
        fetcher = InputFetcher(cache_location)
        data = fetcher.get_input(year, day)

        return cls(data.strip())
        
    def batched_integers(self, batch_size: int) -> Generator[tuple[int, ...], None, None]:
        for batch in batched(INTEGER_REGEX.findall(self.data), batch_size):
            yield map(int, batch)

    def re_integers(self) -> Generator[int, None, None]:
        for n in INTEGER_REGEX.findall(self.data):
            yield int(n)

    def integers(self):
        for n in self.splitlines():
            yield int(n)

    def lines(self) -> Generator["PuzzleInput", None, None]:
        for line in self.splitlines():
            yield PuzzleInput(line)

    def split_integers(self, sep=None) -> Generator[Generator[int, None, None], None, None]:
        for line in self.splitlines():
            yield map(int, line.split(sep))