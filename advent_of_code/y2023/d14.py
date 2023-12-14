from collections import deque

from tinsel import BaseSolution, Processing


class Cycles:
    def __init__(self, window_size=25, min_window=2):
        self.window = []
        self.window_size = window_size
        self.max_size = window_size * 2
        self.min_window = min_window

    def add(self, n: int):
        self.window.append(n)

        if len(self.window) > self.max_size:
            self.window = self.window[1:]

    def check_for_cycles(self):
        for cycle_size in range(self.min_window, self.window_size):
            if len(self.window) > cycle_size * 2:
                lhs = self.window[-cycle_size * 2 : -cycle_size]
                rhs = self.window[-cycle_size:]

                if lhs == rhs:
                    return rhs
            else:
                break


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
        seq = Cycles(min_window=10)

        for wait in range(1, 10000):
            for _ in range(4):
                sat_map = self.rotate(self.tilt_north(sat_map))

            seq.add(self.calculate_weight(sat_map))

            if res := seq.check_for_cycles():
                return wait, res

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        sat_map = [[c for c in line] for line in p.lines()]

        self.sat_map = self.tilt_north(sat_map)

        return self.calculate_weight(self.sat_map)

    def part2(self, puzzle_input: str):
        p = Processing(puzzle_input)

        sat_map = [[c for c in line] for line in p.lines()]

        wait, pattern = self.get_pattern(sat_map)

        target = (1000000000 - wait - 1) % len(pattern)

        return pattern[target]
