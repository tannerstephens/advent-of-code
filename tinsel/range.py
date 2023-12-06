from typing import Optional


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
