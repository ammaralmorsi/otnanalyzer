from generator.utils import OverheadValue


class TCM_STATOverheadGenerator:
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(3))
