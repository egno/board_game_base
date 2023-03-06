import pytest

from board.primitives.coordinate import Coordinate


def test_create_coordinate():
    coordinate = Coordinate(5)
    assert coordinate.value == 5


def test_coordinate_is_frozen():
    coordinate = Coordinate(5)
    with pytest.raises(AttributeError):
        coordinate.value = 10


def test_coordinate_representation():
    coordinate = Coordinate(5)
    assert repr(coordinate) == "5"


@pytest.mark.parametrize(
    "value1, value2, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (-5, -10, -15),
        (100, -50, 50)
    ]
)
def test_coordinate_addition_parametrize(value1, value2, expected):
    coordinate1 = Coordinate(value1)
    coordinate2 = Coordinate(value2)
    result = coordinate1 + coordinate2
    assert result.value == expected
    assert isinstance(result, Coordinate)
