from operator import add, mul
from typing import Callable

from garland import BaseSolution, PuzzleInput
from garland.utils import *


def math_collapse(target: int, values: list[int], ops: list[Callable], c: int = None):
    if c is None:
        c = values.pop(0)

    if len(values) == 0:
        return c == target

    v = values.pop(0)

    for op in ops:
        if math_collapse(target, values[:], ops, op(c, v)):
            return True

    return False

def con(a: int, b: int) -> int:
    return int(f'{a}{b}')

class Solution(BaseSolution):
    def part1(self, puzzle_input: PuzzleInput):
        c = 0

        for line in puzzle_input.lines():
            target, *values = line.re_integers()

            if math_collapse(target, values, [add, mul]):
                c += target

        return c



    def part2(self, puzzle_input: PuzzleInput):
        c = 0

        for line in puzzle_input.lines():
            target, *values = line.re_integers()

            if math_collapse(target, values, [add, mul, con]):
                c += target

        return c
