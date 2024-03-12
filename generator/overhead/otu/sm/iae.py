from generator.utils import OverheadValue, FieldGenerator


class SM_IAEOverheadGenerator(FieldGenerator):
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(1))
