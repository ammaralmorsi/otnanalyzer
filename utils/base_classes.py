from abc import ABC, abstractmethod

from .values import OverheadValue
from .values import PayloadValue


class OverheadGenerator(ABC):
    @property
    @abstractmethod
    def next_value(self) -> OverheadValue:
        pass


class PayloadGenerator(ABC):
    @property
    @abstractmethod
    def next_value(self) -> PayloadValue:
        pass
