import copy
from enum import Enum

from utils.data_classes import OtnField


class OtnOverheads(Enum):
    @classmethod
    def get_fields(cls) -> list[OtnField]:
        return copy.deepcopy([field.value for field in cls])
