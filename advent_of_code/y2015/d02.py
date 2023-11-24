from tinsel import Processing


def surface_area(l: int, w: int, h: int):
    return (2 * l * w) + (2 * w * h) + (2 * h * l)


def part1(puzzle_input):
    p = Processing(puzzle_input)

    area = 0

    for line in p.regex(r"\d+", int):
        s, ss, _ = sorted(line)

        area += surface_area(*line) + (s * ss)

    return area


def part2(puzzle_input):
    p = Processing(puzzle_input)

    feet = 0

    for line in p.regex(r"\d+", int):
        s, ss, t = sorted(line)

        feet += (s + s + ss + ss) + (s * ss * t)

    return feet
