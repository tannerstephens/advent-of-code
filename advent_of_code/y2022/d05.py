from collections import deque
from itertools import islice

from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def process_input(self, puzzle_input: str):
        p = Processing(puzzle_input)

        stack_lines, move_lines = p.split("\n\n", mapping=Processing)

        stack_lines = stack_lines.lines()

        num_stacks = len(stack_lines[-1]) // 4 + 1

        stacks = {i + 1: deque() for i in range(num_stacks)}

        for stack_line in stack_lines[:-1]:
            stack_line = stack_line.ljust(len(stack_lines[-2]))

            for i in range(num_stacks):
                c = stack_line[4 * i + 1]

                if c != " ":
                    stacks[i + 1].appendleft(c)

        moves: list[tuple[int, int, int]] = [(amnt, src, dst) for amnt, src, dst in move_lines.re_findall("\d+", int)]

        return stacks, moves

    def copy_stacks(self, stacks: dict[int, deque]):
        return {name: val.copy() for name, val in stacks.items()}

    def part1(self, puzzle_input: str):
        self.stacks, self.moves = self.process_input(puzzle_input)

        stacks = self.copy_stacks(self.stacks)

        for amnt, src, dst in self.moves:
            for _ in range(amnt):
                stacks[dst].append(stacks[src].pop())

        return "".join(stack.pop() for stack in stacks.values())

    def part2(self, puzzle_input: str):
        for amnt, src, dst in self.moves:
            grabbed = deque()
            for _ in range(amnt):
                grabbed.appendleft(self.stacks[src].pop())

            self.stacks[dst].extend(grabbed)

        return "".join(stack.pop() for stack in self.stacks.values())
