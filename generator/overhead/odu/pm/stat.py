from utils import OverheadGenerator, OverheadValue


class PM_STATOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(3))
