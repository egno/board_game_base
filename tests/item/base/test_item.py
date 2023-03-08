from item.base.item import Item

from board.structure.primitives import Point


def test_place():
    item = Item()
    assert item.point is None
    point = Point(1, 2)
    item.place(point)
    assert item.point == point


def test_remove():
    point = Point(1, 2)
    item = Item(point=point)
    assert item.point == point
    item.remove()
    assert item.point is None
