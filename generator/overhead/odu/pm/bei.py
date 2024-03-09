from generator.utils import OverheadValue


class PM_BEIOverheadGenerator:
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(4))
