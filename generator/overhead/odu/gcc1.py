from utils import OverheadGenerator, OverheadValue


class GCC1OverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(2*8))
