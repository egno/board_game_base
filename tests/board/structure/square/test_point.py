import pytest

from board.structure.square import Orientation, Point


class TestPoint:

    @pytest.mark.parametrize(
        "coordinates, orientation, expected_coordinates",
        [
            ((0, 0), Orientation(0), (0, 0)),
            ((1, 2), Orientation(0), (1, 2)),
            ((1, 2), Orientation(1), (-2, 1)),
            ((1, 2), Orientation(2), (-1, -2)),
            ((1, 2), Orientation(3), (2, -1)),
            ((1, 2), Orientation(4), (1, 2)),
            ((1, 2), Orientation(-3), (-2, 1)),
            ((1, 2), Orientation(-2), (-1, -2)),
            ((1, 2), Orientation(-1), (2, -1)),
            ((-2, 1), Orientation(-1), (1, 2)),
            ((-1, -2), Orientation(-2), (1, 2)),
            ((2, -1), Orientation(-3), (1, 2)),
        ])
    def test_rotate(self, coordinates, orientation, expected_coordinates):
        point = Point(*coordinates)
        rotated_point = point.rotate(orientation)
        expected_point = Point(*expected_coordinates)
        assert isinstance(rotated_point, Point)
        assert rotated_point == expected_point
