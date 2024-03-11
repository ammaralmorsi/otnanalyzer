from generator.utils import OverheadValue


class NullPSIOverheadGenerator:
    def get_next_value(self):
        return OverheadValue(binary_string=f"{int('FD', 16):08b}")