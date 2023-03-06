from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Coordinate:
    value: int = 0

    def __repr__(self) -> str:
        return f'{self.value}'

    def __add__(self, __o: Self) -> Self:
        return self.__class__(self.value + __o.value)

    def __hash__(self) -> int:
        return self.value.__hash__()

    def __neg__(self) -> Self:
        return self.__class__(value=-self.value)

