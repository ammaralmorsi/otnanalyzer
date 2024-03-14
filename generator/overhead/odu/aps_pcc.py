from utils import OverheadGenerator, OverheadValue


class APS_PCCOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(4*8))
