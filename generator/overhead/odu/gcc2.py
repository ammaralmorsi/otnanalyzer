from generator.utils import OverheadValue


class GCC2OverheadGenerator:
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(2*8))
