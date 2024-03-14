from utils import OverheadGenerator, OverheadValue


class ResOverheadGenerator(OverheadGenerator):
    def __init__(self, size:int):
        self.size = size  # in bytes

    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(8*self.size))
