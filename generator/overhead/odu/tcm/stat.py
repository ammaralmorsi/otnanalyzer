from generator.utils import OverheadValue, FieldGenerator


class TCM_STATOverheadGenerator(FieldGenerator):
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(3))
