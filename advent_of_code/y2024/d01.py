from collections import Counter

from garland import BaseSolution, PuzzleInput


class Solution(BaseSolution):
    PART2_DEPENDS_ON_PART1 = True

    def part1(self, puzzle_input: PuzzleInput):
        self.left = []
        self.right = []

        for a, b in puzzle_input.split_integers():
            self.left.append(a)
            self.right.append(b)

        self.left.sort()
        self.right.sort()

        s = 0

        for a, b in zip(self.left, self.right):
            s += abs(a-b)

        return s

    def part2(self, _: PuzzleInput):
        c = Counter(self.right)
        s = 0

        for a in self.left:
            s += (a * c[a])

        return s
