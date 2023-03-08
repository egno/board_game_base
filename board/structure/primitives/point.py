from typing import Callable, Dict, Self, cast

from board.structure.primitives.coordinate import Coordinate
from board.structure.primitives.coordinates import CoordinatesType
from board.structure.primitives.exceptions import (MaxDimensionsException,
                                                   MaxValueException,
                                                   RotationException)
from board.structure.primitives.orientation import Orientation


class Point:
    coordinates: CoordinatesType
    max_bites: int = 10
    max_dimensions: int = 4
    orientation_map: Dict[Orientation, Callable] = {
        Orientation(0): lambda args: args,
    }

    def __init__(self, *args: int | Coordinate) -> None:
        if not args:
            args = (0,)

        if len(args) > self.max_dimensions:
            raise MaxDimensionsException()

        int_args = tuple(
            x.value if isinstance(x, Coordinate) else x
            for x in args
        )
        self.max_value = 2**self.max_bites - 1
        if any([abs(x) > self.max_value for x in int_args]):
            raise MaxValueException()

        self.coordinates = tuple(Coordinate(value) for value in int_args)

    @property
    def dimension(self) -> int:
        return len(self.coordinates)

    def __repr__(self) -> str:
        return " ".join([
            self.__class__.__name__,
            str(self),
        ])

    def __str__(self) -> str:
        return ":".join([
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
        # a collision-safe hash
        return (((
            sum([
                abs(x.value) << (i*self.max_bites)
                for i, x in enumerate(self.coordinates)
            ]) << self.max_dimensions
        ) + sum([
            (x.value > 0) << i for i, x in enumerate(self.coordinates)
        ])) << self.max_dimensions) + len(self.coordinates)

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

    def rotate(self, orientation: Orientation) -> Self:
        func = self.orientation_map.get(orientation)
        if func is None:
            raise RotationException()
        coordinates = func(*self.coordinates)
        return self.__class__(*coordinates)
