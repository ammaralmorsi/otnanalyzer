from utils import OverheadGenerator, OverheadValue


class PM_TTIOverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(8))
