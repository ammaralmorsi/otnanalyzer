from generator.utils import OverheadValue, FieldGenerator


class FASOverheadGenerator(FieldGenerator):
    def get_next_value(self) -> OverheadValue:
        oa1:str = "11110110"
        oa2:str = "00101000"
        return OverheadValue(binary_string=''.join([oa1, oa1, oa1, oa2, oa2, oa2]))
