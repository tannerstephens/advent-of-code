from functools import reduce

from garland import BaseSolution, PuzzleInput

MUL_REGEX = r"mul\((-?\d+),(-?\d+)\)"

class Solution(BaseSolution):
    def part1(self, puzzle_input: PuzzleInput):
        return sum(int(a) * int(b) for a,b in puzzle_input.findall(MUL_REGEX))

    # def part2(self, puzzle_input: PuzzleInput):
    #     states = {0 : True}
    #     for match in puzzle_input.finditer(r"(do\(\)|don't\(\))"):
    #         states[match.end()] = match.group(1) == "do()"

    #     state_keys = states.keys()

    #     s = 0
    #     for match in puzzle_input.finditer(MUL_REGEX):
    #         idex = match.end()
    #         state_key = reduce(lambda x, y: y if y < idex else x, state_keys)
    #         if states[state_key]:
    #             s += int(match.group(1)) * int(match.group(2))

    #     return s

    def part2(self, puzzle_input: PuzzleInput):
        m = True
        s = 0
        for a, b, do, dont in puzzle_input.findall(r"(?:mul\((\d+),(\d+)\)|(do\(\))|(don't\(\)))"):
            if do:
                m = True
            elif dont:
                m = False
            elif m:
                s += int(a) * int(b)

        return s
