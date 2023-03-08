from typing import Optional, Self

from board.structure.primitives import Point
from player import Player


class Item:

    def __init__(self,
                 player: Optional[Player] = None,
                 point: Optional[Point] = None,
                 ) -> None:
        self.point = point
        self.player = player

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

    def place(self, point: Point) -> Self:
        self.point = point
        return self

    def remove(self) -> Self:
        self.point = None
        return self
