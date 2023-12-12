from functools import cache

from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def puzzle_is_valid(self, puzzle: str, clues: tuple[int]) -> bool:
        group_len = 0
        clue_index = 0

        puzzle += "."

        try:
            for c in puzzle:
                if c == ".":
                    if group_len:
                        if group_len != clues[clue_index]:
                            return False
                        clue_index += 1
                        group_len = 0
                elif c == "?":
                    return True
                else:
                    group_len += 1

            return clue_index == len(clues)
        except IndexError:
            return False

    def count_solutions(self, puzzle: str, clues: tuple[int], to_process=-1, clue_index=0, block_length=0, cache=None):
        if "?" not in puzzle:
            return self.puzzle_is_valid(puzzle, clues)

        if clue_index == len(clues):
            return self.puzzle_is_valid(puzzle.replace("?", "."), clues)

        if cache is None:
            cache = {}

        to_process += 1

        cache_key = (to_process, clue_index, block_length)

        if cache_key in cache:
            return cache[cache_key]

        if puzzle[to_process] == "?":
            solutions = 0
            if block_length < clues[clue_index]:
                solutions += self.count_solutions(
                    puzzle.replace("?", "#", 1), clues, to_process, clue_index, block_length + 1, cache
                )
            if block_length == 0:
                solutions += self.count_solutions(puzzle.replace("?", ".", 1), clues, to_process, clue_index, 0, cache)
            elif block_length == clues[clue_index]:
                solutions += self.count_solutions(
                    puzzle.replace("?", ".", 1), clues, to_process, clue_index + 1, 0, cache
                )

            cache[cache_key] = solutions

            return solutions

        elif puzzle[to_process] == "#":
            if (block_length + 1) > clues[clue_index]:
                return 0
            return self.count_solutions(puzzle, clues, to_process, clue_index, block_length + 1, cache)
        else:
            if block_length and block_length < clues[clue_index]:
                return 0
            return self.count_solutions(puzzle, clues, to_process, clue_index + (block_length > 0), 0, cache)

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.puzzles: list[tuple[str, tuple[int]]] = []

        solutions = 0

        for ((puzzle, rhs),) in p.re_findall("(.+) (.+)", lambda s: s):
            clues = tuple(int(i) for i in rhs.split(","))

            self.puzzles.append((puzzle, clues))

            solutions += self.count_solutions(puzzle, clues)

        return solutions

    def part2(self, puzzle_input: str):
        solutions = 0

        for puzzle, clues in self.puzzles:
            expanded_puzzle = "?".join([puzzle] * 5)
            expanded_clues = clues * 5

            solutions += self.count_solutions(expanded_puzzle, expanded_clues)

        return solutions
