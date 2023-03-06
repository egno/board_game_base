from typing import Dict, Final, Self, Callable

from primitives.point import Point as PrimitivePoint
from square.orientation import Orientation


ORIENTATION_MAP: Final[Dict[Orientation, Callable]] = {
    Orientation(0): lambda x, y: (x, y),    # DIRECTION_UP
    Orientation(1): lambda x, y: (-y, x),   # DIRECTION_RIGHT
    Orientation(2): lambda x, y: (-x, -y),  # DIRECTION_DOWN
    Orientation(3): lambda x, y: (y, -x),   # DIRECTION_LEFT
}


class Point(PrimitivePoint):

    def rotate(self, orientation: Orientation) -> Self:
        func = ORIENTATION_MAP[orientation]
        coordinates = func(*self.coordinates)
        return self.__class__(*coordinates)
