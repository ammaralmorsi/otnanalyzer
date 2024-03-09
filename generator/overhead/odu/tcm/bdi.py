from generator.utils import OverheadValue


class TCM_BDIOverheadGenerator:
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(1))
