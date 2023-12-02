from tinsel import Processing


def part1(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    elves = [0]

    for cal in p.integers():
        if cal is None:
            elves.append(0)
        else:
            elves[-1] += cal

    elves.sort(reverse=True)

    state["elves"] = elves

    return elves[0]


def part2(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    return sum(state["elves"][0:3])
