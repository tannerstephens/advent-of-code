from collections import defaultdict

from garland import BaseSolution, PuzzleInput
from garland.utils import *


class Page:
    def __init__(self, n: int, rules) -> None:
        self.n = n
        self.rules = rules

    def __lt__(self, other):
        if self.n in other.rules:
            return True
        else:
            return False

    def __le__(self, other):
        return self < other

    def __repr__(self) -> str:
        return str(self.n)

    def __add__(self, other):
        return self.n + other

    def __radd__(self, other):
        return self.n + other



class Solution(BaseSolution):
    PART2_DEPENDS_ON_PART1 = True

    def part1(self, puzzle_input: PuzzleInput):
        ordering, updates = puzzle_input.split('\n\n')

        ordering_rules = defaultdict(set)

        for line in ordering.lines():
            l, r = line.split_integers('|')
            ordering_rules[r].add(l)

        t = 0

        self.incorrect: list[list[Page]] = []

        for update in updates.lines():
            ints = list(update.split_integers(','))
            ints_set = set(ints)

            pages = [Page(n, ordering_rules[n] & ints_set) for n in ints]

            if is_ordered(pages):
                t += ints[len(ints) // 2]
            else:
                self.incorrect.append(pages)

        return t


    def part2(self, puzzle_input: PuzzleInput):
        t = 0

        for inc in self.incorrect:
            inc.sort()

            t += inc[len(inc) // 2]

        return t
