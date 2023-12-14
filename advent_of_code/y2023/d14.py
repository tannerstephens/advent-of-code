from collections import deque

from tinsel import BaseSolution, Processing


class Cycles:
    def __init__(self, window_size=25):
        self.window = deque()
        self.window_size = window_size
        self.max_size = window_size * 2

    def add(self, n: int):
        self.window.append(n)

        if len(self.window) > self.max_size:
            self.window.popleft()

    def check_for_cycles(self):
        working_window = list(self.window)
        for cycle_size in range(2, min(self.window_size, len(working_window))):
            lhs = working_window[-cycle_size * 2 : -cycle_size]

            if lhs == working_window[-cycle_size:]:
                return lhs


class Solution(BaseSolution):
    def tilt_north(self, sat_map: list[list[str]]) -> list[list[str]]:
        out = []

        stop_index = [0] * len(sat_map[0])

        for y, line in enumerate(sat_map):
            out.append([])

            for x, c in enumerate(line):
                out[-1].append(c)
                if c == "O":
                    if y != stop_index[x]:
                        out[y][x] = "."
                        out[stop_index[x]][x] = "O"

                    stop_index[x] += 1
                elif c == "#":
                    stop_index[x] = y + 1

        return out

    def calculate_weight(self, sat_map: list[list[str]]) -> int:
        inverse = len(sat_map)
        weight = 0

        for y, line in enumerate(sat_map):
            for c in line:
                if c == "O":
                    weight += inverse - y

        return weight

    def rotate(self, sat_map: list[list[str]]):
        return list(zip(*sat_map[::-1]))

    def get_pattern(self, sat_map: list[list[str]]) -> list[int]:
        seq = Cycles()

        wait = 0

        while wait := wait + 1:
            for _ in range(4):
                sat_map = self.rotate(self.tilt_north(sat_map))

            seq.add(self.calculate_weight(sat_map))

            if res := seq.check_for_cycles():
                return wait, res

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.sat_map = [[c for c in line] for line in p.lines()]

        return self.calculate_weight(self.tilt_north(self.sat_map))

    def part2(self, puzzle_input: str):
        wait, pattern = self.get_pattern(self.sat_map)

        return pattern[(999999999 - wait) % len(pattern)]
