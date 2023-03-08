from typing import Optional


class NamedMixin:

    def __init__(self,
                 name: Optional[str] = None,
                 **kwargs,
                 ) -> None:
        self.name = name
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} <{self.name}>"
