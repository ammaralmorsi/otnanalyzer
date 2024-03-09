from generator.utils import OverheadValue


class DMOverheadGenerator:
    def get_next_value(self):
        return OverheadValue(binary_string=''.zfill(1))
