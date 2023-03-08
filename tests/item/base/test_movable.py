import pytest

from board.structure.square import Orientation, Point
from item.base.movable import ItemMoveException, MovableItem
from player import Player


def test_move_exceptions():
    player = Player('player 1', orientation=Orientation(0))
    with pytest.raises(ItemMoveException):
        MovableItem().move(Point(0, 1))
    with pytest.raises(ItemMoveException):
        MovableItem(point=Point(1, 2)).move(Point(0, 1))
    with pytest.raises(ItemMoveException):
        MovableItem(player=player).move(Point(0, 1))


@pytest.mark.parametrize("coordinates, direction, delta, expected", [
    ((1, 2), 0, (0, 1), (1, 3)),
    ((1, 2), 0, (0, -1), (1, 1)),
    ((1, 2), 0, (-1, 0), (0, 2)),
    ((1, 2), 1, (0, 1), (0, 2)),
    ((1, 2), 1, (4, -5), (6, 6)),
])
def test_move(coordinates, direction, delta, expected):
    player = Player('player 1', orientation=Orientation(direction))
    item = MovableItem(
        point=Point(*coordinates),
        player=player,
    ).move(Point(*delta))
    assert item.point == Point(*expected)
