from typing import Final, Set

from square.orientation import Orientation
from square.point import Point


DIRECTION_UP: Final[Point] = Point(1, 0)
DIRECTION_RIGHT: Final[Point] = DIRECTION_UP.rotate(Orientation(1))
DIRECTION_DOWN: Final[Point] = DIRECTION_UP.rotate(Orientation(2))
DIRECTION_LEFT: Final[Point] = DIRECTION_UP.rotate(Orientation(3))

DIRECTIONS_UP_DOWN: Final[Set[Point]] = {
    DIRECTION_UP,
    DIRECTION_DOWN,
}

DIRECTIONS_RIGHT_LEFT: Final[Set[Point]] = {
    DIRECTION_RIGHT,
    DIRECTION_LEFT,
}

DIRECTIONS_4D: Final[
    Set[Point]
] = DIRECTIONS_UP_DOWN ^ DIRECTIONS_RIGHT_LEFT

DIRECTIONS_DIAGONAL_UP: Final[Set[Point]] = {
    DIRECTION_UP + DIRECTION_RIGHT,
    DIRECTION_UP + DIRECTION_LEFT,
}

DIRECTIONS_DIAGONAL_DOWN: Final[Set[Point]] = {
    DIRECTION_DOWN + DIRECTION_RIGHT,
    DIRECTION_DOWN + DIRECTION_LEFT,
}

DIRECTIONS_DIAGONAL: Final[
    Set[Point]
] = DIRECTIONS_DIAGONAL_UP ^ DIRECTIONS_DIAGONAL_DOWN

DIRECTIONS_8D: Final[
    Set[Point]
] = DIRECTIONS_4D ^ DIRECTIONS_DIAGONAL
