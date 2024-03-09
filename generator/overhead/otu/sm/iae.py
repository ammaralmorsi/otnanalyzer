from generator.utils import OverheadValue


class SM_IAEOverheadGenerator:
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(1))
