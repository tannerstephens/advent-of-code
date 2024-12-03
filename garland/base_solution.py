from garland.puzzle_input import PuzzleInput


class BaseSolution:
    PART2_DEPENDS_ON_PART1 = False

    def part1(self, puzzle_input: PuzzleInput):
        raise NotImplementedError()

    def part2(self, puzzle_input: PuzzleInput):
        raise NotImplementedError()
