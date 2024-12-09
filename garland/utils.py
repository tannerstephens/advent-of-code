from enum import Enum


def is_ordered(l: list, desc=False):
    if desc:
        return all(l[i] >= l[i+1] for i in range(len(l) - 1))
    else:
        return all(l[i] <= l[i+1] for i in range(len(l) - 1))

class Direction(Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"

    @property
    def delta(self):
        match self:
            case Direction.NORTH:
                return (0, -1)
            case Direction.EAST:
                return (1, 0)
            case Direction.SOUTH:
                return (0, 1)
            case Direction.WEST:
                return (-1, 0)

    @property
    def left(self):
        match self:
            case Direction.NORTH:
                return Direction.WEST
            case Direction.EAST:
                return Direction.NORTH
            case Direction.SOUTH:
                return Direction.EAST
            case Direction.WEST:
                return Direction.SOUTH
    @property
    def right(self):
        match self:
            case Direction.NORTH:
                return Direction.EAST
            case Direction.EAST:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.WEST
            case Direction.WEST:
                return Direction.NORTH

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value
