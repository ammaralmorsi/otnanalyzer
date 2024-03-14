from utils import OverheadGenerator, OverheadValue


class FixedValueOverheadGenerator(OverheadGenerator):
    def __init__(self, fixed_value: int, size=1):
        self.fixed_value: int = fixed_value
        self.size: int = size

    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=f"{self.fixed_value:08b}" * self.size)
