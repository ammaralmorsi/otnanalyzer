from generator.utils import OverheadValue


class PRBSPSIOverheadGenerator:
    def get_next_value(self):
        return OverheadValue(binary_string=f"{int('FE', 16):08b}")
