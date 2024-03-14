from utils import OverheadGenerator, OverheadValue


class TCM_BEI_BIAEOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(4))
