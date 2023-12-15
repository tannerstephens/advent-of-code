from functools import cache
from typing import Optional

from tinsel import BaseSolution, Processing


class Box:
    def __init__(self, box_id: int):
        self.front: Lens | None = None
        self.back: Lens | None = None

        self._lenses: dict[str, Lens] = {}

        self.id = box_id + 1

    def add_lens(self, lens_label: str, focal_length: int):
        if lens := self._lenses.get(lens_label):
            lens.focal_length = focal_length
        else:
            lens = Lens(focal_length, front=self.back)
            if self.back:
                self.back.back = lens

            self._lenses[lens_label] = lens

        if lens.back is None:
            self.back = lens
        if lens.front is None:
            self.front = lens

    def remove_lens(self, lens_label: str):
        if lens_label in self._lenses:
            lens = self._lenses.pop(lens_label)

            if lens.front is None:
                self.front = lens.back
            if lens.back is None:
                self.back = lens.front

            lens.delete()

    def __iter__(self):
        lens = self.front
        while lens:
            yield lens
            lens = lens.back

    def __repr__(self) -> str:
        s = f"Box {self.id}:"

        for lens in self:
            s += f" [{lens.label} {lens.focal_length}]"

        return s


class Lens:
    def __init__(
        self,
        focal_length: int | None = None,
        front: Optional["Lens"] = None,
        back: Optional["Lens"] = None,
    ):
        self.focal_length = focal_length

        self.front = front
        self.back = back

    def delete(self):
        if self.front:
            self.front.back = self.back

        if self.back:
            self.back.front = self.front

        self.front = None
        self.back = None


class Solution(BaseSolution):
    @cache
    def get_hash(self, s: str) -> int:
        current_value = 0

        for c in s:
            current_value += ord(c)
            current_value *= 17
            current_value %= 256

        return current_value

    def part1(self, puzzle_input: str):
        return sum(self.get_hash(s) for s in puzzle_input.strip().split(","))

    def part2(self, puzzle_input: str):
        p = Processing(puzzle_input)

        boxes: dict[int, Box] = {}

        for label, op, foc_len in p.re_findall(r"(.+?)([=-])(\d+)?,?", mapping=lambda s: s):
            label_hash = self.get_hash(label)

            if label_hash not in boxes:
                boxes[label_hash] = Box(label_hash)

            box = boxes[label_hash]

            if op == "=":
                box.add_lens(label, int(foc_len))
            else:
                box.remove_lens(label)

        return sum((box.id) * i * lens.focal_length for box in boxes.values() for i, lens in enumerate(box, 1))
