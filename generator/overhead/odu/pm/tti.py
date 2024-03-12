from generator.utils import OverheadValue, FieldGenerator


class PM_TTIOverheadGenerator(FieldGenerator):
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(8))
