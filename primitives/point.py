from typing import Self, cast

from primitives.coordinate import Coordinate
from primitives.coordinates import CoordinatesType


class Point:
    coordinates: CoordinatesType

    def __init__(self, *args: int) -> None:
        if not args:
            args = (0,)

        self.coordinates = tuple(Coordinate(value) for value in args)

    @property
    def dimension(self) -> int:
        return len(self.coordinates)

    def __repr__(self) -> str:
        return ' '.join([
            self.__class__.__name__,
            str(self),
        ])

    def __str__(self) -> str:
        return ':'.join([
            coordinate.__repr__()
            for coordinate
            in self.coordinates
        ])

    def __eq__(self, __o: object) -> bool:
        if not self.same_type(__o):
            return False
        return self.coordinates == cast(Self, __o).coordinates

    def __add__(self, __o: object) -> Self:
        if not self.same_type(__o):
            return NotImplemented
        return self.move(cast(Self, __o))

    def __sub__(self, __o: object) -> Self:
        if not self.same_type(__o):
            return NotImplemented
        return self.move(-cast(Self, __o))

    def __mul__(self, __i: int) -> Self:
        new_coordinates = tuple(
            a.value * __i
            for a
            in self.coordinates
        )
        return self.__class__(*new_coordinates)

    def __neg__(self) -> Self:
        new_coordinates = tuple(
            -a.value
            for a
            in self.coordinates
        )
        return self.__class__(*new_coordinates)

    def __hash__(self) -> int:
        return self.coordinates.__hash__()

    def move(self, delta: Self) -> Self:
        new_coordinates = tuple(
            (a+b).value
            for a, b
            in zip(self.coordinates, delta.coordinates)
        )
        return self.__class__(*new_coordinates)

    def same_type(self, __o: object) -> bool:
        return all([
            isinstance(__o, self.__class__),
            self.dimension == cast(Self, __o).dimension,
        ])
