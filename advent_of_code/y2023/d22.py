from dataclasses import dataclass

from tinsel import BaseSolution, Processing


@dataclass
class Brick:
    x: int
    y: int
    z: int
    l: int
    w: int
    h: int
    id: str

    _len_key = lambda _, val: (val, 0, 0)
    _wid_key = lambda _, val: (0, val, 0)
    _dep_key = lambda _, val: (0, 0, val)

    def __post_init__(self):
        self.init_block_deltas()

    def __hash__(self):
        return hash(self.id)

    def init_block_deltas(self):
        self.block_deltas: list[tuple[int, int, int]] = []

        if self.l:
            rng = self.l
            key = self._len_key
        elif self.w:
            rng = self.w
            key = self._wid_key
        else:
            rng = self.h
            key = self._dep_key

        for val in range(rng + 1):
            self.block_deltas.append(key(val))

    def highest_point(self):
        return self.z + self.h

    @property
    def blocks(self):
        for dx, dy, dz in self.block_deltas:
            yield (self.x + dx, self.y + dy, self.z + dz)

    def on_ground(self):
        for _, _, z in self.blocks:
            if z == 1:
                return True

        return False

    def on(self, brick2: "Brick"):
        if brick2 is self:
            return False

        for b1x, b1y, b1z in self.blocks:
            for b2x, b2y, b2z in brick2.blocks:
                if b1x == b2x and b1y == b2y and (b1z - 1) == b2z:
                    return True
        return False

    def bricks_resting_on(self, bricks: list["Brick"]):
        if self.on_ground():
            return []

        resting = []

        for brick in bricks:
            if self.on(brick):
                resting.append(brick)

        return resting

    def can_fall(self, bricks):
        if self.on_ground():
            return False

        for brick in bricks:
            if self.on(brick):
                return False

        return True

    def fall(self):
        self.z -= 1

    def __repr__(self) -> str:
        return f"B({self.id})"


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.bricks: list[Brick] = []

        for brick_id, (x0, y0, z0, x1, y1, z1) in enumerate(p.re_findall(r"\d+", int)):
            l = x1 - x0
            w = y1 - y0
            h = z1 - z0

            self.bricks.append(Brick(x0, y0, z0, l, w, h, brick_id))

        self.bricks.sort(key=lambda brick: brick.z)

        short_fall = 0
        removable = set(self.bricks)

        self.resting: dict[Brick, set[Brick]] = {}

        for i, brick in enumerate(self.bricks):
            if short_fall:
                brick.z = short_fall + 1
            analysis_bricks = self.bricks[:i]
            while brick.can_fall(analysis_bricks):
                brick.fall()

            self.resting[brick] = set(brick.bricks_resting_on(analysis_bricks))

            if len(self.resting[brick]) == 1:
                removable.discard(next(iter(self.resting[brick])))

            short_fall = max(brick.highest_point(), short_fall)

        return len(removable)

    def remove_brick(self, brick: Brick, resting: dict[Brick, set[Brick]] | None = None):
        fall = 0

        if resting is None:
            resting = {b: r.copy() for b, r in self.resting.items()}

        check = []

        for brick2, r in resting.items():
            if brick in r:
                r.remove(brick)

                check.append(brick2)

        for brick2 in check:
            if len(resting[brick2]) == 0:
                fall += self.remove_brick(brick2, resting) + 1

        return fall

    def part2(self, puzzle_input: str):
        return sum(self.remove_brick(brick) for brick in self.bricks)
