from abc import ABC
from typing import Optional

from board.structure.primitives import Point
from player import Player


class Item(ABC):

    def __init__(self,
                 player: Optional[Player] = None,
                 point: Optional[Point] = None,
                 ) -> None:
        self.point = point
        self.player = player

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"
