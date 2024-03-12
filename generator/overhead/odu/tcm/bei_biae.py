from generator.utils import OverheadValue, FieldGenerator


class TCM_BEI_BIAEOverheadGenerator(FieldGenerator):
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(4))
