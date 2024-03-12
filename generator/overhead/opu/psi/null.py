from generator.utils import OverheadValue, FieldGenerator


class NullPSIOverheadGenerator(FieldGenerator):
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=f"{int('FD', 16):08b}")
