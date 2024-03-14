from utils import OverheadGenerator, OverheadValue


class PM_BEIOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(4))
