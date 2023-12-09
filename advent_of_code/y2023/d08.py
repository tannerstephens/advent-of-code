from itertools import cycle
from math import lcm

from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def parse_input(self, puzzle_input: str):
        p = Processing(puzzle_input)

        node_map = {}

        insts, nodes = p.split("\n\n", mapping=Processing)

        for key, left, right in nodes.re_findall(r"\w+"):
            node_map[key] = dict(left=left, right=right)

        insts = [("left" if inst == "L" else "right") for inst in insts]

        return insts, node_map

    def steps_to_z(self, node_name):
        for count, inst in enumerate(cycle(self.insts)):
            if node_name[-1] == "Z":
                return count

            node_name = self.node_map[node_name][inst]

    def part1(self, puzzle_input: str):
        self.insts, self.node_map = self.parse_input(puzzle_input)

        return self.steps_to_z("AAA")

    def part2(self, puzzle_input: str):
        starting_nodes = [node for node in self.node_map if node[-1] == "A"]

        return lcm(*(self.steps_to_z(snode) for snode in starting_nodes))
