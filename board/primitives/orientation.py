from typing import Optional, Self, cast


class Orientation:

    def __init__(self,
                 discretness: int,
                 value: Optional[int] = None,
                 ) -> None:
        self.discretness = discretness
        self.value = ((value or 0) + self.discretness) % self.discretness

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {self}'

    def __str__(self) -> str:
        return f'{self.value}/{self.discretness}'

    def __add__(self, __o: Self) -> Self:
        if not self.same_type(__o):
            return NotImplemented
        return self.__class__(
            discretness=self.discretness,
            value=self.value + __o.value,
        )

    def __sub__(self, __o: Self) -> Self:
        if not self.same_type(__o):
            return NotImplemented
        return self.__class__(
            discretness=self.discretness,
            value=self.value - __o.value,
        )

    def __hash__(self) -> int:
        return self.value

    def __eq__(self, __o: object) -> bool:
        if not self.same_type(__o):
            return False
        return self.value == cast(Self, __o).value

    def __neg__(self) -> Self:
        return self.__class__(
            discretness=self.discretness,
            value=-self.value,
        )

    def same_type(self, __o: object) -> bool:
        return all([
            isinstance(__o, self.__class__),
            self.discretness == cast(Self, __o).discretness,
        ])
