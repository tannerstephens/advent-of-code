from math import prod

from tinsel import BaseSolution, Processing


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        s = 0

        self.games = {}

        for game in p.lines(Processing):
            game_id = game.re_search(r"\d+", mapping=int)

            self.games[game_id] = {
                "red": max(game.re_findall(r"(\d+) red", int)),
                "green": max(game.re_findall(r"(\d+) green", int)),
                "blue": max(game.re_findall(r"(\d+) blue", int)),
            }

            if (
                self.games[game_id]["red"] <= 12
                and self.games[game_id]["green"] <= 13
                and self.games[game_id]["blue"] <= 14
            ):
                s += game_id

        return s

    def part2(self, puzzle_input: str):
        return sum(prod(game.values()) for game in self.games.values())
