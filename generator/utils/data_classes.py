from dataclasses import dataclass, field
from .base_classes import FieldGenerator


@dataclass
class Position:
    col:int
    row:int


@dataclass
class Dimension:
    nrows:int
    ncols:int


@dataclass
class OtnField:
    name:str
    position:Position
    dimension:Dimension
    generator:FieldGenerator = field(default_factory=FieldGenerator)

    def __repr__(self) -> str:
        return f"{self.name}\n{self.position}\n{self.dimension}\n"

    def __hash__(self) -> int:
        return hash(self.name)
