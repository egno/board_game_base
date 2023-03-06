import pytest

from board.primitives.point import Point, MaxDimensionsError, MaxValueError


@pytest.mark.parametrize("point_args, expected_repr", [
    ((1, 2, 3), "Point 1:2:3"),
    ((0, 0), "Point 0:0"),
    ((-1, -2, -3), "Point -1:-2:-3"),
    ((0, 0, 0, 0), "Point 0:0:0:0"),
])
def test_point_representation(point_args, expected_repr):
    point = Point(*point_args)
    assert repr(point) == expected_repr
    assert point.dimension == len(point_args)


@pytest.mark.parametrize("point_arg, expected_repr", [
    (1, "Point 1"),
    (0, "Point 0"),
    (-1023, "Point -1023"),
])
def test_single_point_representation(point_arg, expected_repr):
    point = Point(point_arg)
    assert repr(point) == expected_repr
    assert point.dimension == 1


@pytest.mark.parametrize("point_args, expected_hash", [
    ((1, 2, 3), 805831027),
    ((0, 0), 2),
    ((-1, -2, -3), 805830915),
    ((0, 0, 0, 0), 4),
    ((-1023, -1023, -1023, -1023), 281474976710404),
    ((1023, 1023, 1023, 1023), 281474976710644),
])
def test_point_hash(point_args, expected_hash):
    point = Point(*point_args)
    assert point.__hash__() == expected_hash


@pytest.mark.parametrize("point_args, expected_exception", [
    ((1025,), MaxValueError),
    ((-1025,), MaxValueError),
    ((0, 1025), MaxValueError),
    ((0, -1025), MaxValueError),
    ((0, 0, 0, 0, 0), MaxDimensionsError),
])
def test_point_exceptions(point_args, expected_exception):
    with pytest.raises(expected_exception):
        Point(*point_args)


@pytest.mark.parametrize("point_args, result_point", [
    ((1, 2, 3), (-1, -2, -3)),
    ((0, 0), (0, 0)),
    ((-1, -2, -3), (1, 2, 3)),
    ((0, -4, 5, -1), (0, 4, -5, 1)),
])
def test_point_negative(point_args, result_point):
    point1 = Point(*point_args)
    point2 = Point(*result_point)
    assert -point1 == point2


@pytest.mark.parametrize("point_args, mul, result_point", [
    ((1, 2, 3), 2, (2, 4, 6)),
    ((0, 0), 2, (0, 0)),
    ((-1, -2, -3), 2, (-2, -4, -6)),
    ((0, -4, 5, -1), 2, (0, -8, 10, -2)),
    ((1, 2, 3), 0, (0, 0, 0)),
    ((0, 0), 2, (0, 0)),
    ((1, 2, 3), -1, (-1, -2, -3)),
    ((0, 0), -1, (0, 0)),
    ((-1, -2, -3), -1, (1, 2, 3)),
    ((0, -4, 5, -1), -1, (0, 4, -5, 1)),
])
def test_point_mul(point_args, mul, result_point):
    point1 = Point(*point_args)
    point2 = Point(*result_point)
    assert point1 * mul == point2


@pytest.mark.parametrize("point1_args, point2_args, expected_point", [
    ((1, 2), (3, 4), Point(4, 6)),
    ((-1, 2), (4, -2), Point(3, 0)),
    ((0, 0), (0, 0), Point(0, 0)),
])
def test_point_move(point1_args, point2_args, expected_point):
    point1 = Point(*point1_args)
    point2 = Point(*point2_args)
    new_point = point1.move(point2)
    assert new_point == expected_point


@pytest.mark.parametrize("point1_args, point2_args, expected_point", [
    ((1, 2), (3, 4), Point(4, 6)),
    ((-1, 2, 3), (4, -2, 1), Point(3, 0, 4)),
    ((0, 0), (0, 0), Point(0, 0)),
])
def test_point_add(point1_args, point2_args, expected_point):
    point1 = Point(*point1_args)
    point2 = Point(*point2_args)
    new_point = point1 + point2
    assert new_point == expected_point


@pytest.mark.parametrize("point1_args, point2_args, expected_point", [
    ((1, 2), (3, 5), Point(-2, -3)),
    ((-1, 2, 3), (4, -2, 1), Point(-5, 4, 2)),
    ((0, 0), (0, 0), Point(0, 0)),
])
def test_point_sub(point1_args, point2_args, expected_point):
    point1 = Point(*point1_args)
    point2 = Point(*point2_args)
    new_point = point1 - point2
    assert new_point == expected_point


@pytest.mark.parametrize("point1_args, point2_args", [
    ((1, 2), (3, 4, 3)),
    ((-1, 2, 3), (4, -2)),
])
def test_point_add_exceptions(point1_args, point2_args):
    point1 = Point(*point1_args)
    point2 = Point(*point2_args)
    with pytest.raises(TypeError):
        point1 + point2


@pytest.mark.parametrize("point1_args, point2_args, expected_eq", [
    ((1, 2), (1, 2), True),
    ((1, 2), (1, 2, 0), False),
    ((1, 2, 0), (1, 2), False),
    ((1, 2), (3, 4), False),
    ((1, 2, 3), (-1, -2, -3), False),
])
def test_point_eq(point1_args, point2_args, expected_eq):
    point1 = Point(*point1_args)
    point2 = Point(*point2_args)
    assert (point1 == point2) == expected_eq
