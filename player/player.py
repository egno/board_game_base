from typing import Optional

from board.structure.primitives import Orientation


class Player:

    def __init__(self,
                 name: str,
                 orientation: Optional[Orientation] = None,
                 ) -> None:
        self.name = name
        self.orientation = orientation or Orientation(0)
