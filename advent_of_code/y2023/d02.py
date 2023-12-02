from tinsel import Processing
from math import prod


def part1(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    t = 0

    max_colors = {"red": 12, "green": 13, "blue": 14}

    for nums, colors in zip(p.findall(r"\d+", int), p.findall(r" ([a-z]+)")):
        pos = True
        for num, color in zip(nums[1:], colors):
            if num > max_colors[color]:
                pos = False
                break

        t += pos * nums[0]

    return t


def part2(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    t = 0

    for nums, colors in zip(p.findall(r"\d+", int), p.findall(r" ([a-z]+)")):
        maxes = {"red": 0, "green": 0, "blue": 0}

        for num, color in zip(nums[1:], colors):
            maxes[color] = max(maxes[color], num)

        t += prod(maxes.values())

    return t
