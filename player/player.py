from board.structure.primitives import Orientation


class Player:

    def __init__(self,
                 name: str,
                 orientation: Orientation,
                 ) -> None:
        self.name = name
        self.orientation = orientation
