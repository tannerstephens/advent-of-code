from functools import lru_cache

from tinsel import Processing


@lru_cache
def pressure_released(cave_map: dict, open_nodes: set[str]):
    return sum(cave_map[cave]["rate"] for cave in open_nodes)


def release_pressure(
    cave_map: dict,
    current_node: str = "AA",
    pressure: int = 0,
    steps: int = 30,
    open_nodes: set[str] | None = None,
):
    if steps == 0:
        return pressure

    open_nodes = open_nodes or set()

    if current_node not in open_nodes and cave_map[current_node]["rate"]:
        new_open_nodes = open_nodes + [current_node]
        release_pressure(
            cave_map,
            current_node=current_node,
            pressure=pressure + pressure_released(cave_map, new_open_nodes),
            steps=steps-1,
            open_nodes=new_open_nodes
        )


def part1(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)

    cave_map = {}

    for caves, rate in zip(p.findall(r"[A-Z]{2}"), p.search(r"\d+", int)):
        cave_map[caves[0]] = {"rate": rate, "paths": caves[1:]}

    state["cave_map"] = cave_map


def part2(puzzle_input: str, state: dict):
    p = Processing(puzzle_input)
