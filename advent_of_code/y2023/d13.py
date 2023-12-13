from collections import deque

from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def has_reflection(self, pattern: deque[str], target_diff=0) -> int | None:
        bottom = pattern.copy()
        top: deque[str] = deque()

        while len(bottom) > 1:
            top.append(bottom.popleft())
            len_iter = min(len(top), len(bottom))
            mirror = True
            diff = 0

            for i in range(len_iter):
                if top[-i - 1] != bottom[i]:
                    for c1, c2 in zip(top[-i - 1], bottom[i]):
                        diff += c1 != c2

                    if diff > target_diff:
                        mirror = False
                        break

            if mirror and (diff == target_diff):
                return len(top)

        return None

    def rotate_pattern(self, pattern: deque[str]):
        return deque("".join(line) for line in zip(*pattern))

    def get_notes(self, pattern: deque[str], target_diff=0) -> int:
        if row := self.has_reflection(pattern, target_diff):
            return row * 100
        else:
            return self.has_reflection(self.rotate_pattern(pattern), target_diff)

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.patterns: list[deque[str]] = []

        notes = 0

        for pattern in p.split("\n\n", mapping=lambda s: deque(s.splitlines())):
            self.patterns.append(pattern)
            notes += self.get_notes(pattern)

        return notes

    def part2(self, puzzle_input: str):
        return sum(self.get_notes(pattern, 1) for pattern in self.patterns)
