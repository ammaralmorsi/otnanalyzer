from generator.utils import OverheadValue, FieldGenerator


class GCC2OverheadGenerator(FieldGenerator):
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(2*8))
