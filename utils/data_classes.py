from typing import Union
from dataclasses import dataclass, field

from .base_classes import OverheadGenerator, PayloadGenerator
from .field_types import OtnFieldTypes


@dataclass
class Position:
    row: int
    col: int


@dataclass
class Dimension:
    nrows: int
    ncols: int
    size: int = field(init=False)

    def __post_init__(self):
        self.size = self.nrows * self.ncols


@dataclass
class OtnField:
    name: str
    field_type: OtnFieldTypes
    position: Position
    dimension: Dimension
    inner_fields: list["OtnField"] = field(default_factory=list)
    generator: Union[OverheadGenerator, PayloadGenerator] = field(init=False)

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)
