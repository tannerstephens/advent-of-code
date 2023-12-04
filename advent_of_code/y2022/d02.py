from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def part1(self, puzzle_input: str, points=None):
        p = Processing(puzzle_input)

        if points is None:
            points = {
                "A X": 4,
                "A Y": 8,
                "A Z": 3,
                "B X": 1,
                "B Y": 5,
                "B Z": 9,
                "C X": 7,
                "C Y": 2,
                "C Z": 6,
            }

        score = 0

        for line in p.lines():
            score += points[line]

        return score

    def part2(self, puzzle_input: str):
        return self.part1(
            puzzle_input,
            {
                "A X": 3,
                "A Y": 4,
                "A Z": 8,
                "B X": 1,
                "B Y": 5,
                "B Z": 9,
                "C X": 2,
                "C Y": 6,
                "C Z": 7,
            },
        )
