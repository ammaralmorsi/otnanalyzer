from generator.utils import OverheadValue, FieldGenerator


class ExpOverheadGenerator(FieldGenerator):
    def __init__(self, size:int):
        # size in bytes
        self.size = size

    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(8*self.size))
