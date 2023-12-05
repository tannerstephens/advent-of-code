from typing import Optional

from tinsel import BaseSolution, Processing


class Range:
    def __init__(self, start: int, end: int | None = None, length: int | None = None):
        self.start = start
        self.end = end or (self.start + length - 1)

    def __repr__(self) -> str:
        return f"Range({self.start} -> {self.end})"

    @property
    def length(self):
        return self.end - self.start + 1

    def contains(self, target: "Range"):
        return (self.start <= target.start) and (self.end >= target.end)

    def intersects(self, target: "Range"):
        return (self.start <= target.end) and (target.start <= self.end)

    def __contains__(self, key):
        return self.start <= key <= self.end

    def divmod(self, divisor: "Range") -> tuple[Optional["Range"], list["Range"]]:
        if not self.intersects(divisor):
            return (None, [self])

        if divisor.contains(self):
            return (self, [])

        div = Range(max(self.start, divisor.start), end=min(self.end, divisor.end))
        mod = []

        if divisor.start > self.start:
            mod.append(Range(self.start, end=divisor.start))

        if divisor.end < self.end:
            mod.append(Range(divisor.end, end=self.end))

        return (div, mod)

    def translate(self, distance: int):
        self.start += distance
        self.end += distance


class Solution(BaseSolution):
    GROUP_KEYS = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]

    def parse_input(self, puzzle_input: str) -> tuple[dict[str, list[list[int]]], list[int]]:
        p = Processing(puzzle_input)

        group_keys = ["seeds"] + self.GROUP_KEYS

        groups = {}

        for i, group in enumerate(p.split("\n\n", mapping=Processing)):
            groups[group_keys[i]] = [item for item in group.re_findall(r"\d+", int) if (item == 0 or item)]

        seeds = groups.pop("seeds")

        return groups, seeds

    def next_seed_val(self, seed: int, mappings: list[list[int]]):
        for to, fr, r in mappings:
            if fr <= seed < (fr + r):
                return seed + (to - fr)

        return seed

    def evolve_seeds(self, seeds: list[int], groups: dict):
        for group_mappings in groups.values():
            for i in range(len(seeds)):
                seeds[i] = self.next_seed_val(seeds[i], group_mappings)

        return seeds

    def part1(self, puzzle_input: str):
        self.groups, self.seeds = self.parse_input(puzzle_input)

        return min(self.evolve_seeds(self.seeds[:], self.groups))

    def expand_groups(self, groups: dict[str, list[list[int]]]) -> dict[str, list[dict[str, Range]]]:
        expanded_groups = {}

        for group_name, group_items in groups.items():
            expanded_groups[group_name] = []

            for dst, src, r in group_items:
                expanded_groups[group_name].append(
                    {"src": Range(src, length=r), "dst": Range(dst, length=r), "off": dst - src}
                )

        return expanded_groups

    def expand_seeds(self, seeds: list[int]):
        expanded_seeds = []
        for i in range(0, len(seeds), 2):
            expanded_seeds.append(Range(seeds[i], length=seeds[i + 1]))

        return expanded_seeds

    def process_seed_ranges(self, seeds: list[Range], groups: dict[str, list[dict[str, Range]]]):
        for group in groups.values():
            new_seeds = []

            for seed in seeds:
                check = [seed]
                for group_item in group:
                    next_check = []
                    for check_seed in check:
                        div, mod = check_seed.divmod(group_item["src"])
                        next_check.extend(mod)

                        if div:
                            div.translate(group_item["off"])
                            new_seeds.append(div)

                    check = next_check
                new_seeds.extend(check)

            seeds = new_seeds

        return seeds

    def part2(self, puzzle_input: str):
        expanded_groups = self.expand_groups(self.groups)
        expanded_seeds = self.expand_seeds(self.seeds)

        return min(self.process_seed_ranges(expanded_seeds, expanded_groups), key=lambda seed: seed.start).start
