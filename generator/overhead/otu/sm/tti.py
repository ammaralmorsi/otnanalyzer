from utils import OverheadGenerator, OverheadValue


class SM_TTIOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(8))
