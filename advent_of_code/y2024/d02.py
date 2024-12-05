from garland import BaseSolution, PuzzleInput


def is_ordered(levels: list[int]):
    if all(levels[i] <= levels[i+1] for i in range(len(levels) - 1)):
        return True

    return all(levels[i] >= levels[i+1] for i in range(len(levels) - 1))

def is_safe(levels: list[int]):
    for i in range(len(levels) - 1):
        a = levels[i]
        b = levels[i + 1]

        if not (1 <= abs(a-b) <= 3):
            return False

    if not is_ordered(levels):
        return False

    return True


class Solution(BaseSolution):
    PART2_DEPENDS_ON_PART1 = True

    def part1(self, puzzle_input: PuzzleInput):

        self.safe = 0
        self.unsafe = []

        for report in puzzle_input.lines():
            lv = list(report.split_integers())

            if is_safe(lv):
                self.safe += 1
            else:
                self.unsafe.append(lv)

        return self.safe


    def part2(self, _: PuzzleInput):
        safe = 0

        for levels in self.unsafe:
            for removal in range(len(levels)):
                new_levels = levels[:removal] + levels[removal+1:]

                if is_safe(new_levels):
                    safe += 1
                    break


        return safe + self.safe
