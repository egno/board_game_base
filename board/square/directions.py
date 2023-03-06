from typing import Final, Set

from board.square.orientation import Orientation
from board.square.point import Point


DIRECTION_UP: Final[Point] = Point(1, 0)
DIRECTION_RIGHT: Final[Point] = DIRECTION_UP.rotate(Orientation(1))
DIRECTION_DOWN: Final[Point] = DIRECTION_UP.rotate(Orientation(2))
DIRECTION_LEFT: Final[Point] = DIRECTION_UP.rotate(Orientation(3))

DIRECTION_UP_RIGHT: Final[Point] = DIRECTION_UP + DIRECTION_RIGHT
DIRECTION_UP_LEFT: Final[Point] = DIRECTION_UP + DIRECTION_LEFT
DIRECTION_DOWN_RIGHT: Final[Point] = DIRECTION_DOWN + DIRECTION_RIGHT
DIRECTION_DOWN_LEFT: Final[Point] = DIRECTION_DOWN + DIRECTION_LEFT


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
    DIRECTION_UP_RIGHT,
    DIRECTION_UP_LEFT,
}

DIRECTIONS_DIAGONAL_DOWN: Final[Set[Point]] = {
    DIRECTION_DOWN_RIGHT,
    DIRECTION_DOWN_LEFT,
}

DIRECTIONS_DIAGONAL: Final[
    Set[Point]
] = DIRECTIONS_DIAGONAL_UP ^ DIRECTIONS_DIAGONAL_DOWN

DIRECTIONS_8D: Final[
    Set[Point]
] = DIRECTIONS_4D ^ DIRECTIONS_DIAGONAL


class Direction:
    UP = DIRECTION_UP
    RIGHT = DIRECTION_RIGHT
    DOWN = DIRECTION_DOWN
    LEFT = DIRECTION_LEFT
    UP_RIGHT = DIRECTION_UP_RIGHT
    UP_LEFT = DIRECTION_UP_LEFT
    DOWN_RIGHT = DIRECTION_DOWN_RIGHT
    DOWN_LEFT = DIRECTION_DOWN_LEFT


class DirectionSet:
    UP_DOWN = DIRECTIONS_UP_DOWN
    RIGHT_LEFT = DIRECTIONS_RIGHT_LEFT
    CROSS = DIRECTIONS_4D
    DIAGONAL_UP = DIRECTIONS_DIAGONAL_UP
    DIAGONAL_DOWN = DIRECTIONS_DIAGONAL_DOWN
    DIAGONAL = DIRECTIONS_DIAGONAL
    ALL = DIRECTIONS_8D
