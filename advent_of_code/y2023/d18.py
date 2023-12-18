from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    INSTS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

    def area(self, insts: list[tuple[str, int]]):
        x1 = y1 = 0

        top = 0
        points = 2

        for inst, amnt in insts:
            dx, dy = self.INSTS[inst]
            x2, y2 = x1 + (dx * (amnt)), y1 + (dy * (amnt))

            top += (x1 * y2) - (y1 * x2)
            points += amnt

            x1, y1 = x2, y2

        return (top - points) // 2 + points

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.colors = []

        insts = []

        for ((inst, amnt, color),) in p.re_findall(r"(.) (\d+) \(#(.+)\)", mapping=lambda s: s):
            amnt = int(amnt)
            self.colors.append(color)

            insts.append((inst, amnt))

        return self.area(insts)

    INT_TO_INST = ["R", "D", "L", "U"]

    def color_to_inst(self, color: str) -> tuple[str, int]:
        inst = self.INT_TO_INST[int(color[-1])]
        amnt = int(color[:-1], 16)

        return (inst, amnt)

    def part2(self, puzzle_input: str):
        return self.area(self.color_to_inst(color) for color in self.colors)
