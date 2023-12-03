from math import prod

from tinsel import Processing


def part1(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    s = 0

    for game in p.lines():
        game: Processing

        game_id = game.re_search(r"\d+", mapping=int)

        state[game_id] = {
            "red": max(game.re_findall(r"(\d+) red", int)),
            "green": max(game.re_findall(r"(\d+) green", int)),
            "blue": max(game.re_findall(r"(\d+) blue", int)),
        }

        if (
            state[game_id]["red"] <= 12
            and state[game_id]["green"] <= 13
            and state[game_id]["blue"] <= 14
        ):
            s += game_id

    return s


def part2(puzzle_input: str, state: dict[int, dict[str, int]]):
    return sum(prod(game.values()) for game in state.values())
