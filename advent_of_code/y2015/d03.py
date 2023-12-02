from tinsel import Processing

dirs = {"^": (0, 1), "v": (0, -1), "<": (-1, 0), ">": (1, 0)}


def part1(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    x = y = 0

    m = {(0, 0)}

    for d in p:
        dx, dy = dirs[d]

        x += dx
        y += dy

        m.add((x, y))
    return len(m)


def part2(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    x = rx = y = ry = 0

    m = {(0, 0)}

    for ds, dr in p.grouped_chars(2):
        dxs, dys = dirs[ds]
        dxr, dyr = dirs[dr]

        x += dxs
        y += dys

        rx += dxr
        ry += dyr

        m.add((x, y))
        m.add((rx, ry))

    return len(m)
