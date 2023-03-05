from typing import Final, Optional

from primitives.orientation import Orientation as PrimitiveOrientation

MAX_DISCRETENESS: Final[int] = 3


class Orientation(PrimitiveOrientation):

    def __init__(self, value: Optional[int] = None) -> None:
        super().__init__(MAX_DISCRETENESS, value)
