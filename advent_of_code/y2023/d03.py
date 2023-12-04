from collections import defaultdict

from tinsel import Processing

SYMBOLS = set("!@#$%^&*()_+-=/")


def part1(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    grid = p.to_grid()

    s = 0

    state["gears"] = defaultdict(list)

    for y, line in enumerate(p.re_finditer(r"\d+")):
        for match in line:
            x = match.start()

            for c, cx, cy in grid.indexed_neighbors(x, y, bw=(match.end() - x)):
                if c in SYMBOLS:
                    s += (val := int(match.group(0)))
                    if c == "*":
                        state["gears"][(cx, cy)].append(val)

                    break

    return s


def part2(puzzle_input: str, state: dict[str, dict[tuple[int, int], list[int]]]):
    return sum(
        parts[0] * parts[1] for parts in state["gears"].values() if len(parts) == 2
    )
