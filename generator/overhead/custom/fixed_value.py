from generator.utils import OverheadValue, FieldGenerator


class FixedValueOverheadGenerator(FieldGenerator):
    def __init__(self, fixed_value:int):
        self.fixed_value:int = fixed_value

    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=f"{self.fixed_value:08b}")
