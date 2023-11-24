from tinsel import Processing


def part1(puzzle_input):
    p = Processing(puzzle_input)

    return p.count("(") - p.count(")")


def part2(puzzle_input):
    p = Processing(puzzle_input)

    floor = 0

    for i, c in enumerate(p):
        floor += 1 if c == "(" else -1

        if floor < 0:
            return i + 1
