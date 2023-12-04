from types import SimpleNamespace


class BaseSolution:
    def __init__(self) -> None:
        self.state = SimpleNamespace()

    def part1(self, puzzle_input: str):
        raise NotImplementedError()

    def part2(self, puzzle_input: str):
        raise NotImplementedError()
