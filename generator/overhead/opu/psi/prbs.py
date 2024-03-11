from generator.utils import OverheadValue


class PRBSPSIOverheadGenerator:
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=f"{int('FE', 16):08b}")
