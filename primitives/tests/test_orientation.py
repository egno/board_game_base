import pytest

from primitives.orientation import Orientation


@pytest.mark.parametrize(
    "discretness, value, expected_value", [
        (4, None, 0),
        (4, 3, 3),
        (4, 13, 1),
        (4, -3, 1),
        (4, -13, 3),
    ]
)
def test_orientation_init(discretness, value, expected_value):
    o = Orientation(discretness=discretness, value=value)
    assert o.value == expected_value
    assert o.discretness == discretness


@pytest.mark.parametrize(
    "o1_discretness, o1_value, o2_discretness, o2_value, operation, expected_value",  # noqa E501
    [
        (4, 3, 4, 5, "__add__", 0),
        (4, 3, 4, 5, "__sub__", 2),
        (4, 3, 3, 2, "__add__", NotImplemented),
        (4, 3, 3, 2, "__sub__", NotImplemented),
    ]
)
def test_orientation_operations(o1_discretness, o1_value, o2_discretness,
                                o2_value, operation, expected_value):
    o1 = Orientation(discretness=o1_discretness, value=o1_value)
    o2 = Orientation(discretness=o2_discretness, value=o2_value)
    result = getattr(o1, operation)(o2)
    if expected_value == NotImplemented:
        assert result == NotImplemented
    else:
        assert result.value == expected_value
        assert result.discretness == o1.discretness


@pytest.mark.parametrize(
    "o1_discretness, o1_value, o2_discretness, o2_value, expected_result", [
        (4, 3, 4, 3, True),
        (4, 3, 4, -1, True),
        (4, 3, 4, 5, False),
        (4, 3, 3, 3, False),
    ]
)
def test_orientation_eq(o1_discretness, o1_value, o2_discretness, o2_value,
                        expected_result):
    o1 = Orientation(discretness=o1_discretness, value=o1_value)
    o2 = Orientation(discretness=o2_discretness, value=o2_value)
    assert (o1 == o2) == expected_result


@pytest.mark.parametrize(
    "discretness, value, expected_value", [
        (4, 3, 1),
        (4, 0, 0),
    ]
)
def test_orientation_neg(discretness, value, expected_value):
    o = Orientation(discretness=discretness, value=value)
    result = -o
    assert result.value == expected_value
    assert result.discretness == o.discretness
