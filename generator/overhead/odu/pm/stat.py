from generator.utils import OverheadValue


class PM_STATOverheadGenerator:
    def get_next_value(self):
        return OverheadValue(binary_string=''.zfill(3))
