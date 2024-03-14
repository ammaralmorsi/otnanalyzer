from utils import OverheadGenerator, OverheadValue


class PJOOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(8))
