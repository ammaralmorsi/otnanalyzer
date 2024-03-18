from __future__ import annotations  # for python version compatibilty issues

from typing import Optional, Union

from dataclasses import dataclass, field

from .base_classes import OtnFieldGenerator
from .field_types import OtnFieldTypes, OtnPayloadTypes


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
    field_type: Union[OtnFieldTypes, OtnPayloadTypes]
    position: Position
    dimension: Dimension
    inner_fields: list["OtnField"] = field(default_factory=list)
    generator: OtnFieldGenerator = field(init=False)

    def __post_init__(self):
        self.generator = None  # FIXME: OtnFrameConfig no generator attribute

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)


@dataclass
class OtnFrame:
    position: Position
    dimension :Dimension
    payload: OtnField
    overheads: list[OtnField]

    def set_payload_type(self, payload_type: OtnPayloadTypes) -> None:
        self.payload.field_type = payload_type
        self.payload.name = payload_type.name

    def __hash__(self) -> int:
        return hash(self.payload)
