from generator.utils import OverheadValue


class SM_TTIOverheadGenerator:
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(8))