from string import ascii_letters

from tinsel import Processing

PRIORITY = {c: i + 1 for i, c in enumerate(ascii_letters)}


def part1(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    total = 0

    for line in p.lines():
        half = len(line) // 2
        total += PRIORITY[(set(line[:half]) & set(line[half:])).pop()]

    return total


def part2(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    total = 0

    for l1, l2, l3 in p.grouped_lines(3):
        total += PRIORITY[(set(l1) & set(l2) & set(l3)).pop()]

    return total
