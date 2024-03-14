from utils import OverheadGenerator, OverheadValue


class SM_IAEOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(1))
