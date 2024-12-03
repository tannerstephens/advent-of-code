import os
from argparse import ArgumentParser, Namespace
from functools import cached_property
from importlib import import_module
from pathlib import Path
from shutil import copy
from timeit import default_timer
from typing import Literal

from .base_solution import BaseSolution
from .input_fetcher import InputFetcher
from .puzzle_input import PuzzleInput

DAY_TEMPLATE = Path(__file__).parent.resolve() / '_templates' / 'day_template.py'

class Runner:
    def __init__(self, solutions_package: str = "advent_of_code"):
        self._init_solutions_package(solutions_package)

    def _init_solutions_package(self, solutions_package: str) -> None:
        self.solutions_package = solutions_package
        self.solutions_package_path = Path.cwd() / self.solutions_package

        self.solutions_package_path.mkdir(exist_ok=True)
        (self.solutions_package_path / "__init__.py").touch()

    class Args(Namespace):
        year: int | None
        day: int | None
        part: int | None

        create: bool
        input: str | None
        all: bool
        view_input: bool

    @cached_property
    def args(self):
        self.parser = ArgumentParser()

        self.parser.add_argument("year", nargs="?", default=None, type=int)
        self.parser.add_argument("day", nargs="?", default=None, type=int)
        self.parser.add_argument("part", nargs="?", default=None, type=int, choices=[1, 2])

        self.parser.add_argument("-c", "--create", action="store_true")
        self.parser.add_argument("-i", "--input")
        self.parser.add_argument("-A", "--all", action="store_true")
        self.parser.add_argument("-V", "--view-input", action="store_true")

        return self.parser.parse_args(namespace=self.Args)
    
    def _left_pad(self, data: str, pad: int):
        pad = " " * pad

        return "\n".join(f"{pad}{line}" for line in data.splitlines())
    
    def _load_day(self, year: int, day: int) -> BaseSolution:
        module_path = self._day_path(year, day)

        if not module_path.exists():
            raise Exception(f"The solution for y{year}/d{day:>02} does not exist")

        module = import_module(f"{self.solutions_package}.y{year}.d{day:>02}")

        return module.Solution()
    
    def _time_method(self, method, *args, **kwargs):
        begin_time = default_timer()
        res = method(*args, **kwargs)
        end_time = default_timer()

        runtime = end_time - begin_time

        return res, runtime * 1000
    
    def _run_day(
        self,
        year: int,
        day: int,
        part: Literal[1, 2] | None = None,
        pad: int = 0,
        puzzle_input: str | None = None,
    ) -> float:
        day_solution = self._load_day(year, day)

        if puzzle_input:
            puzzle_input = PuzzleInput(puzzle_input)
        else:
            puzzle_input = PuzzleInput.from_day(year, day)

        padding = " " * pad

        print(f"{padding}Day {day:>02}")

        part1_time = part2_time = 0

        if part is None or part == 1 or day_solution.PART2_DEPENDS_ON_PART1:
            part1_res, part1_time = self._time_method(day_solution.part1, puzzle_input)
            print(f"{padding}  Part 1 - ({part1_time:.2f} ms)")
            print(self._left_pad(str(part1_res), 4 + pad), "\n")

        if part is None or part == 2:
            part2_res, part2_time = self._time_method(day_solution.part2, puzzle_input)
            print(f"{padding}  Part 2 - ({part2_time:.2f} ms)")
            print(self._left_pad(str(part2_res), 4 + pad), "\n")

        return part1_time + part2_time
    
    def _view_input(self, year: int, day: int) -> None:
        input_fetcher = InputFetcher()
        input_file = input_fetcher._get_input_file(year, day)
        input_fetcher.get_input(year, day)

        if not input_file.exists():
            raise Exception("No input file available")

        os.spawnlp(os.P_WAIT, "nano", "nano", "--view", input_file)

    def _year_path(self, year: int) -> Path:
        return self.solutions_package_path / f"y{year}"

    def _day_path(self, year: int, day: int) -> Path:
        return self._year_path(year) / f"d{day:>02}.py"

    def _init_year(self, year: int) -> None:
        year_path = self._year_path(year)

        year_path.mkdir(exist_ok=True)
        (year_path / "__init__.py").touch()

    def _init_day(self, year: int, day: int, force=False) -> None:
        self._init_year(year)

        day_path = self._day_path(year, day)

        if day_path.exists() and not force:
            raise Exception(f"Solution file y{year}/d{day:>02} already exists!")

        copy(DAY_TEMPLATE, day_path)
    
    def _get_latest_year(self) -> int:
        return max(int(path.name[-4:]) for path in self.solutions_package_path.glob("y*"))
    
    def _get_all_days(self, year) -> list[int]:
        return [int(path.name[-5:-3]) for path in self.solutions_package_path.glob(f"y{year}/d*.py")]
    
    def _get_latest_day(self, year) -> int | None:
        if days := self._get_all_days(year):
            return max(days)

        return None
    
    def _get_next_day(self, year) -> int:
        latest = self._get_latest_day(year) or 0

        return latest + 1
    
    def _run_all_days(self, year: int) -> float:
        days = self._get_all_days(year)

        print(f"Year {year}")

        total_time = 0

        for day in sorted(days):
            total_time += self._run_day(year, day, pad=2)

        print(f"Total Time - {total_time:.2f} ms ({total_time / (len(days)*2):.2f} ms / part)")

        return total_time
        

    def run(self):
        year = self.args.year or self._get_latest_year()

        if self.args.view_input:
            day = self.args.day or self._get_latest_day(year)

            self._view_input(year, day)

        elif self.args.create:
            day = self.args.day or self._get_next_day(year)

            self._init_day(year, day)

        elif self.args.year is None or self.args.day is not None:
            day = self.args.day or self._get_latest_day(year) or 1

            self._run_day(year, day, self.args.part, puzzle_input=self.args.input)

        else:
            self._run_all_days(year)