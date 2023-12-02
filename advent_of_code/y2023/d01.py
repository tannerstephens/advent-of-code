from itertools import product

from tinsel import Processing


def part1(puzzle_input: str, state: dict):
    ALL_VALUES = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    PRECOMP = {
        l + r: int(ALL_VALUES[l] + ALL_VALUES[r])
        for l, r in product(ALL_VALUES.keys(), repeat=2)
    }

    p = Processing(puzzle_input)

    return sum(
        PRECOMP[l + r]
        for l, r in zip(p.search(r"\d"), p.search(r"(\d)\D*$", group=True))
    )


def part2(puzzle_input: str, state: dict):
    ALL_VALUES = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    PRECOMP = {
        l + r: int(ALL_VALUES[l] + ALL_VALUES[r])
        for l, r in product(ALL_VALUES.keys(), repeat=2)
    }

    p = Processing(puzzle_input)

    return sum(
        PRECOMP[line[0] + line[-1]]
        for line in p.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    )
