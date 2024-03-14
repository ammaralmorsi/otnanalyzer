from utils import OverheadGenerator, OverheadValue


class PRBSPSIOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=f"{int('FE', 16):08b}")
