from utils import OverheadGenerator, OverheadValue


class TCM_STATOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(3))
