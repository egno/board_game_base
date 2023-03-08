from board.structure.primitives import Point as PrimitivePoint
from board.structure.square.orientation import Orientation


class Point(PrimitivePoint):
    orientation_map = {
        Orientation(0): lambda x, y: (x, y),    # DIRECTION_UP
        Orientation(1): lambda x, y: (-y, x),   # DIRECTION_RIGHT
        Orientation(2): lambda x, y: (-x, -y),  # DIRECTION_DOWN
        Orientation(3): lambda x, y: (y, -x),   # DIRECTION_LEFT
    }
