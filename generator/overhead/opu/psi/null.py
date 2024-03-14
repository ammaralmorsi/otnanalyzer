from utils import OverheadGenerator, OverheadValue


class NullPSIOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=f"{int('FD', 16):08b}")
