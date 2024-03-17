from abc import ABC, abstractmethod
from typing import Union

from .values import OverheadValue
from .values import PayloadValue
from .values import FrameValue


class OtnFieldGenerator(ABC):
    @property
    @abstractmethod
    def next_value(self) -> Union[OverheadValue, PayloadValue, FrameValue]:
        pass


class OverheadGenerator(OtnFieldGenerator):
    @property
    @abstractmethod
    def next_value(self) -> OverheadValue:
        pass


class PayloadGenerator(OtnFieldGenerator):
    @property
    @abstractmethod
    def next_value(self) -> PayloadValue:
        pass


class FrameGenerator(OtnFieldGenerator):
    @property
    @abstractmethod
    def next_value(self) -> FrameValue:
        pass
