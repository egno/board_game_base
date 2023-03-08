from typing import Optional, Self, Set

from board.structure.primitives import Point
from item.base.item import Item


class ItemMoveException(Exception):
    pass


class MovableItem(Item):
    allowed_moves: Optional[Set[Point]] = None

    def check_move(self, delta: Point):
        if self.allowed_moves is None:
            return
        if delta not in self.allowed_moves:
            raise ItemMoveException

    def move(self, delta: Point) -> Self:
        if self.point is None:
            raise ItemMoveException

        if self.player is None:
            raise ItemMoveException

        self.check_move(delta)
        self.point = self.point + delta.rotate(self.player.orientation)

        return self
