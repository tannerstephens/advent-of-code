import os
from argparse import ArgumentParser
from importlib import import_module
from pathlib import Path
from shutil import copy
from time import time
from typing import Any, Protocol, cast

from .input import Input
from .solution import BaseSolution

DAY_TEMPLATE = Path(__file__).parent.resolve() / "_templates" / "day_template.py"


class CLI:
    """Class for handling the running of advent of code puzzle solutions from the CLI"""

    DEFAULT_SOLUTIONS_PACKAGE = "advent_of_code"

    def __init__(self, solutions_package: str | None = None) -> None:
        self._init_parser()
        self._init_solutions_package(solutions_package)

        self.input_handler = Input()

    def _init_parser(self) -> None:
        self.parser = ArgumentParser()

        self.parser.add_argument("year", nargs="?", default=None, type=int)
        self.parser.add_argument("day", nargs="?", default=None, type=int)

        self.parser.add_argument("-c", "--create", action="store_true")
        self.parser.add_argument("-i", "--input")
        self.parser.add_argument("-A", "--all", action="store_true")
        self.parser.add_argument("-V", "--view", action="store_true")

    def _init_solutions_package(self, solutions_package: str | None) -> None:
        self.solutions_package = solutions_package or self.DEFAULT_SOLUTIONS_PACKAGE
        self.solutions_package_path = Path.cwd() / self.solutions_package

        self.solutions_package_path.mkdir(exist_ok=True)
        (self.solutions_package_path / "__init__.py").touch()

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

    def _load_day(self, year: int, day: int) -> BaseSolution:
        module_path = self._day_path(year, day)

        if not module_path.exists():
            raise Exception(f"The solution for y{year}/d{day:>02} does not exist")

        module = import_module(f"{self.solutions_package}.y{year}.d{day:>02}")

        return module.Solution()

    def _get_latest_year(self) -> int:
        return max(int(path.name[-4:]) for path in self.solutions_package_path.glob("y*"))

    def _get_all_years(self) -> list[int]:
        return [int(path.name[1:]) for path in self.solutions_package_path.glob(f"y*")]

    def _get_all_days(self, year) -> list[int]:
        return [int(path.name[-5:-3]) for path in self.solutions_package_path.glob(f"y{year}/d*.py")]

    def _get_latest_day(self, year) -> int | None:
        if days := self._get_all_days(year):
            return max(days)

        return None

    def _get_next_day(self, year) -> int:
        latest = self._get_latest_day(year) or 0

        return latest + 1

    def _time_method(self, method, *args, **kwargs):
        begin_time = time()
        res = method(*args, **kwargs)
        end_time = time()

        runtime = end_time - begin_time

        return res, runtime * 1000

    def _left_pad(self, data: str, pad: int):
        pad = " " * pad

        return "\n".join(f"{pad}{line}" for line in data.splitlines())

    def _view_input(self, year: int, day: int) -> None:
        input_file = self.input_handler._get_input_file(year, day)
        self.input_handler.get_input(year, day)

        if not input_file.exists():
            raise Exception("No input file available")

        os.spawnlp(os.P_WAIT, "nano", "nano", "--view", input_file)

    def run_day(
        self,
        year: int,
        day: int,
        pad: int | None = None,
        puzzle_input: str | None = None,
    ) -> float:
        if pad is None:
            pad = 0

        day_solution = self._load_day(year, day)

        puzzle_input = puzzle_input or self.input_handler.get_input(year, day)

        padding = " " * pad

        print(f"{padding}Day {day:>02}")

        part1_res, part1_time = self._time_method(day_solution.part1, puzzle_input)
        print(f"{padding}  Part 1 - ({part1_time:.2f} ms)")
        print(self._left_pad(str(part1_res), 4 + pad), "\n")

        part2_res, part2_time = self._time_method(day_solution.part2, puzzle_input)
        print(f"{padding}  Part 2 - ({part2_time:.2f} ms)")
        print(self._left_pad(str(part2_res), 4 + pad), "\n")

        return part1_time + part2_time

    def run_all_days(self, year: int) -> float:
        days = self._get_all_days(year)

        print(f"Year {year}")

        total_time = 0

        for day in sorted(days):
            total_time += self.run_day(year, day, pad=2)

        print(f"Total Time - {total_time:.2f} ms ({total_time / (len(days)*2):.2f} ms / part)")

        return total_time

    def run_all_solutions(self):
        all_years_time = 0
        print("Running all completed solutions")
        for year in sorted(self._get_all_years()):
            print()
            all_years_time += self.run_all_days(year)

        print(f"Total time for all solutions - {all_years_time:.2f} ms")

    def _edit_day(self, year: int, day: int):
        day_path = self._day_path(year, day)
        os.execlp("code", "code", ".", day_path)

    def run(self) -> None:
        args = self.parser.parse_args()

        year = args.year or self._get_latest_year()

        if args.view:
            day = args.day or self._get_latest_day(year) or 1

            self._view_input(year, day)
            return

        if args.all:
            self.run_all_solutions()
            return

        if args.create:
            day = args.day or self._get_next_day(year)

            self._init_day(year, day)
            self._edit_day(year, day)
            return

        if args.year is None or args.day is not None:
            day = args.day or self._get_latest_day(year) or 1

            self.run_day(year, day, puzzle_input=args.input)
            return

        self.run_all_days(year)
